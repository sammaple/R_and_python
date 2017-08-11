# -*- coding: utf-8 -*-
"""
导出人物关系对应gexf
生成的tags_douban.gexf需要去掉graphs的标签
@author: juling.jhy
"""

from simplegexf import Gexf, Edge
import pandas as pd
import numpy as np
from pandas import DataFrame

gexf = Gexf('tags_douban.gexf')

#dd = pd.DataFrame()
#da = pd.DataFrame()

try:
    graph = gexf.graphs[0]
except IndexError:
    graph = gexf.add_graph(defaultedgetype="directed")

# Define Graph attributes
graph.define_attributes([
('modularity_class', 'integer'),
])
# Define Edge attributes for Graph
graph.define_attributes([
('relation_type', 'string'),
], _class='edge')

dd = pd.read_csv("director_count.csv", delimiter=',', header=0)
da = pd.read_csv("actor_count_relation.csv", delimiter=',', header=0)

tags = []
for i in range(len(dd)):
    dict = {'id': i, 'name': dd.Director[i], 'modularity_class':int(dd.Rank[i]), 'value': dd.Count[i]}
    tags.append(dict)
#del D:\new\R\douban\echart\tags_douban.gexf

def strToList(str):
    tt = str.split(",")
    l = []
    for t in tt:
        print(t)
        print(type(t))
        if  t.strip()!="":
            l.append(int(t))

    return l

for i in range(len(da)):
    j = i +len(dd)
    dict = {'id': j, 'name': da.Actor[i], 'modularity_class':int(da.Rank[i]), 'value': da.Count[i],'parents':strToList(da.Parent[i])}
    tags.append(dict)


print(tags)
#exit()
nodes = {node.id: node for node in graph.nodes}

'''tags = [
    {
        'id': 0,
        'name': 'Test tag 1',
        'description': 'This is a test tag',
    },
    {
        'id': 1,
        'name': 'Test tag 2',
        'description': 'This is a test tag',
        'parents': [0],
    },
    {
        'id': 2,
        'name': 'Test tag 3',
        'description': 'This is a test tag',
        'parents': [0, 1],
    }
]'''

# Create nodes for tags:
for tag in tags:
    try:
        # See if node exists:
        node = nodes[str(tag['id'])]
    except KeyError:
        # Create a new node:
        node = graph.add_node(id=str(tag['id']), label=tag['name'])
    # Update node:
    node.set('viz:size', value=tag['value'])
    node.set('viz:color', r=130, g=130, b=130)

    # Update node attributes:
    for attr in graph.node_attributes.keys():
        #print(attr)
        try:
            #print(tag[attr])
            node.attributes[attr] = tag[attr]
        except KeyError:
            #print("err")
            try:
                del node.attributes[attr]
            except IndexError:
                pass

nodes = {node.id: node for node in graph.nodes}

# Create edges for tags:
for tag in tags:
    try:
        for parent_id in tag['parents']:
            edge = Edge(parent_id, tag['id'])
            graph.edges.append(edge)
            # Attributes are not available before adding edge to graph
            edge.attributes['relation_type'] = 'parents'
    except KeyError:
        pass

#graph.sort_nodes(attr='count', reverse=True)

gexf.write()