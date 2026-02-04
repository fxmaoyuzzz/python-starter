#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/2/4
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : 12_serialize.py


import json


# json模块有四个比较重要的函数，分别是：
#
# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}


import requests

def weather():
    resp = requests.get('https://apis.tianapi.com/tianqi/index?key=API_KEY&city=上海&type=1')
    if resp.status_code == 200:
        data_model = resp.json()
        print(data_model)
        result = data_model['result']
        # print(result['date'])
        # print(result['province'])
        # print(result['weather'])
        for key in result:
            print(f'{key}:{result[key]}')




if __name__ == '__main__':
    # with open('/Users/fxmaoyuzzz/workspace/data.json', 'w') as file:
    #     json.dump(my_dict, file)

    # with open('/Users/fxmaoyuzzz/workspace/data.json', 'r') as file:
    #     my_dict = json.load(file)
    #     print(type(my_dict))
    #     print(my_dict)
    weather()