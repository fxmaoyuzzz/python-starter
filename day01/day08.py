#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/1/23
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : day08.py


# 字典

# 字典中的键必须是不可变类型，例如整数（int）、浮点数（float）、字符串（str）、元组（tuple）等类型

def dict_test():
    dict1 = {
        'name': 'jack',
        'age': 18,
        'sex': '男'
    }
    print(dict1)  # {'name': 'jack', 'age': 18, 'sex': '男'}

    # 内置 dict 函数创建
    student = dict(name='Tom', age=20, sex='男')
    print(student)  # {'name': 'Tom', 'age': 20, 'sex': '男'}
    # 内置函数zip压缩两个序列并创建字典
    dict2 = dict(zip('ABCDEFG', '1234567'))
    print(dict2)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7'}
    # 当键值对数量不一致时，只输出匹配的键值或有值的键
    dict3 = dict(zip('ABCDEFG', '1234'))
    dict4 = dict(zip('ABC', '1234567'))
    print(dict3)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4'}
    print(dict4)  # {'A': '1', 'B': '2', 'C': '3'}

    # 用字典生成式语法创建字典
    dict5 = {x: x**3 for x in range(1,10)}
    print(dict5)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}

    print(len(dict1))  # 输出：3，键值对数量

    for index in dict1:
        print(index)  # 输出：键

    # 成员运算
    print('name' in  dict1) # True
    print('name' not in  dict1) # False

    # 索引运算
    print(dict1['name']) # 输出：jack
    # print(dict1['name1']) # 键不存在时报错：KeyError: 'name1'

    # 遍历
    for key in dict1:
        print(f'{key}:{dict1[key]}')

    print("遍历方式二")
    for key, value in dict1.items():
        print(f'{key}:{value}')

    # 字典方法
    # 获取值 get
    print(dict1.get("name")) # 输出：jack
    print(dict1.get("name1")) # 输出：None， 跟索引运算不同的是，get方法在字典中没有指定的键时不会产生异常，而是返回None或指定的默认值

    print(dict1.keys())  # dict_keys(['name', 'age', 'sex'])
    print(dict1.values()) #  dict_values(['jack', 18, '男'])
    print(dict1.items())  # dict_items([('name', 'jack'), ('age', 18), ('sex', '男')])

    # 合并方法 update
    dict6 = {'name':'Tom', 'age':30}
    dict7 = {'name':'Tom1', 'age':20, 'sex':'none'}
    dict6.update(dict7)
    print(dict6) # {'name': 'Tom1', 'age': 20, 'sex': 'none'}，相同键值覆盖，不同的新增合并
    # Python 3.9 及以上的版本，也可以使用|运算符来完成同样的操作
    dict6 = {'name':'Tom22', 'age':30}
    dict7 = {'name':'Tom33', 'age':60, 'sex':'none'}
    dict7 |= dict6
    print(dict7)  # {'name': 'Tom22', 'age': 30, 'sex': 'none'}

    # 删除方法 pop 或 popitem
    dict7.pop('name')
    # dict7.pop('name1') # 如果指定的键不存在会报错：KeyError: 'name1'
    print(dict7) # {'age': 30, 'sex': 'none'}
    print(dict7.popitem()) # ('sex', 'none')，Python 3.7 及以上删除最后插入的键值对；Python 3.6 及以下随机删除一个键值对

    del dict6['name']
    # del dict6['name1'] # 指定的键不存在会报错：KeyError: 'name1'

if __name__ == '__main__':
    dict_test()
