# -*- coding: utf-8 -*-
"""
生成人物（导演、演员的产出）及关系对应表
@author: juling.jhy
"""
import json
import pandas as pd
import numpy as np
from pandas import DataFrame

def store(file,data):
    with open(file, 'w') as json_file:
        json_file.write(json.dumps(data))

def load(file):
    with open(file, encoding="utf-8") as json_file:
        data = json.load(json_file, encoding="utf-8")
        return data

def quchong(l1) :
    l2 = []
    for i in l1:
        temp = i.strip()#去掉空额
        if not temp in l2:
            l2.append(temp)
    return l2


def covent_dict_to_dataframe(dicts):
        df = pd.DataFrame()
        i = 0
        for dict in dicts:
            tmp = str(dict).replace("\'","\"")
            #print (tmp)
            tmp_df = pd.DataFrame(json.loads(tmp, encoding="utf-8"), index=[i])
            tmp_df["date"] = tmp_df["date"].str.replace("(","")
            tmp_df["date"] = tmp_df["date"].str.replace(")","")

            #print(tmp_df["director"])
            '''tmp_df["price"] = tmp_df["price"].astype("int")
            tmp_df["area"] = tmp_df["area"].astype("float")
            tmp_df["lng"] = tmp_df["lng"].astype("float")
            tmp_df["lat"] = tmp_df["lat"].astype("float")
            if tmp_df.iloc[0]["time_unit"] == "每天":
                tmp_df.price[i] = tmp_df.price[i] * 30'''

            df = df.append(tmp_df)
            i += 1
        return df

df = load('douban_utf8.json')
df_obj = DataFrame(df)
result_obj_series = df_obj.result

#new_json#重新组装
'''
new_json = "["
for i in result_obj_series :
    new_json +=i
new_json += "]"
'''
result_obj_final =covent_dict_to_dataframe(result_obj_series)
#print(result_obj_final.head())

#http://www.cnblogs.com/CQ-LQJ/p/4909920.html
#print(result_obj_final[result_obj_final["director"].str.contains("伍迪·艾伦")]) 查找某一条内容
directors = result_obj_final["director"]
actors = result_obj_final["actor"]
print(type(directors))
print(type(actors))

dd = pd.DataFrame(columns=['Director',  'Count', 'Rank'])
da = pd.DataFrame(columns=['Actor',  'Count', 'Rank', 'Parent'])
directors_list = []
actors_list = []
'''
遍历导演
'''
for d in directors:
    #for i in d.split(" "):
    tmp2 = d.replace(" ","")
    directors_list += tmp2.split(" ")

'''
遍历演员
'''
for d in actors:
    # for i in d.split(" "):
    tmp = d.replace(" 更多...","")
    tmp2 = tmp.replace(" ","")
    actors_list += tmp2.split("/")

directors_list_uniq = quchong(directors_list)
actors_list_uniq = quchong(actors_list)

dd["Director"] = directors_list_uniq
da["Actor"] = actors_list_uniq

#da.to_csv("director_count.csv")
#exit()

print(len(directors_list))
print(len(directors_list_uniq))#对导演进行去重

print(len(actors_list))
print(len(actors_list_uniq))#对演员进行去重
#print(actors_list.count("江口洋介"))
#exit()


#data frame 是按列读取的
for i  in range(len(directors_list_uniq)) :
    # #len(result_obj_final[result_obj_final["director"].str.contains(d["Director"])])
    # print(dd.Director[i])
    dd.Count[i] = len(result_obj_final[result_obj_final["director"].str.contains(dd.Director[i])])
    if dd.Count[i] >=7 :
        dd.Rank[i] = 0#color
    else :
        dd.Rank[i] = 1
    i += 1

#data frame 是按列读取的
for i  in range(len(actors_list_uniq)) :
    # print(dd.Director[i])
    da.Count[i] = actors_list.count(da.Actor[i])
    if da.Count[i] >=11 :
        da.Rank[i] = 2#color
    else :
        da.Rank[i] = 3
    i += 1

#exit()

dd["Count"] = dd["Count"].astype("int")#申明类型
da["Count"] = da["Count"].astype("int")#申明类型

#print(dd.nlargest(30, columns='Count'))#排序选出前30个
#print(da.nlargest(30, columns='Count'))#排序选出前30个
dd.nlargest(30, columns='Count').to_csv("director_count.csv",encoding="utf-8")
#da.nlargest(30, columns='Count').to_csv("actor_count.csv")

top_30_dd = dd.nlargest(30, columns='Count')
top_30_da = da.nlargest(30, columns='Count')
top_30_da.Parent = ""#初始化
'''
判断2个列表信息
'''
def isDirectorIn(str, list):
    tmp2 = str.replace(" ", "")
    t_list = tmp2.split(" ")
    for i in t_list:
        if i in list:
            return True
    return False

#a = 0
#d = 0

#print(type(top_30_da.Actor))
#print(list(top_30_da.Actor)[0])
#print(type(list(top_30_da.Actor)[0]))
#exit()

for a in range(len(top_30_da)) :
    #if a > 1 : break
    for d in range(len(top_30_dd)) :
        for i in range(len(result_obj_final)) :
            #print(i)
            detail = result_obj_final[i:i+1]
            #print(detail["actor"].str)
            #print(list(top_30_da.Actor)[a])
            #print(list(detail["actor"].str.contains(list(top_30_da.Actor)[a]))[0])
            #exit()
            if list(detail["actor"].str.contains(list(top_30_da.Actor)[a]))[0]\
                    and list(detail["director"].str.contains(list(top_30_dd.Director)[d]))[0]:
                try:
                    top_30_da.Parent[a:a+1]  += ","+ str(d)
                except KeyError:
                    # Create a new node:
                    top_30_da.Parent[a:a+1] = str(d)

                print(top_30_da.Parent[a:a+1])
                #print(type(top_30_da.Parent[a]))
                #print(top_30_da[a:a+2])

                #exit()
        #d += 1
    #a += 1
    #d = 0

print(top_30_da)
top_30_da.to_csv("actor_count_relation.csv",encoding="utf-8")