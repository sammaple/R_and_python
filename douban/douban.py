# -*- coding: utf-8 -*-
"""

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
        if not i in l2:
            l2.append(i)
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
#print(result_obj_final)
print(result_obj_final.head())

#http://www.cnblogs.com/CQ-LQJ/p/4909920.html
#print(result_obj_final[result_obj_final["director"].str.contains("伍迪·艾伦")]) 查找某一条内容
directors = result_obj_final["director"]
print(type(directors))

dd = pd.DataFrame(columns=['Director',  'Count'])
j = []
for d in directors:
    #for i in d.split(" "):
     j += d.split(" ")

print(len(j))
print(len(quchong(j)))#对导演进行去重

dd["Director"] = quchong(j)

#data frame 是按列读取的
for i  in range(len(quchong(j))) :
    #d["Count"] = d["Count"].astype("int")
    # #len(result_obj_final[result_obj_final["director"].str.contains(d["Director"])])
    print(dd.Director[i])
    dd.Count[i] = len(result_obj_final[result_obj_final["director"].str.contains(dd.Director[i])])
    i+=1

print(dd)
dd.to_csv("director_count.csv")