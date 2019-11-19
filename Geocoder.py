# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:23:59 2019

@author: melvi
"""

import pandas as pd
import json
from urllib.request import urlopen,quote

geocoder = pd.DataFrame(columns=['Community','Latitude','Longitude'])
latitude = []
longitude = []
community_list = []
def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoding/v3/?address='
    output = 'json'
    ak = 'wTl5hzGKb78gkK2YMyhyro0jCz4sCQLi'#需填入自己申请应用后生成的ak
    add = quote(address)#本文城市变量为中文，为防止乱码，先用quote进行编码
    url2 = url+add+'&output='+output+"&ak=" +ak
    req = urlopen(url2)
    res  = req.read().decode()
    temp = json.loads(res)
    lng = temp['result']['location']['lng']#获取经度
    lat = temp['result']['location']['lat']
    #str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) +'}'
    #print(str_temp)
    community_list.append(community)
    latitude.append(lat)
    longitude.append(lng)
    #return str_temp

#file = open('C:/Users/melvi/Desktop/Capstone/new4.json','w')#建立json数据文件
data_1 = pd.read_excel("C:/Users/melvi/Desktop/Capstone/Missing again.xlsx", encoding = "gbk")#读取小区房价信息
i = 0
for community in data_1["Community"]:
    community=community.strip()
    getlnglat(community)
    i = i + 1
    print(i)
    
geocoder["Community"] = community_list
geocoder["Latitude"] = latitude
geocoder["Longitude"] = longitude
    

geocoder.to_csv("C:/Users/melvi/Desktop/Capstone/filled again1.csv",encoding = "gbk")    
