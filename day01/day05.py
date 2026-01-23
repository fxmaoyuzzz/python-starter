#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/1/23
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : day05.py


#  元组

# 元组也是多个元素按照一定顺序构成的序列。
# 元组和列表的不同之处在于，元组是[不可变]类型，元组类型的变量一旦定义，其中的元素不能再添加或删除
# 而且元素的值也不能修改。如果试图修改元组中的元素，将引发TypeError错误

def tuple_test():
    tuple_1 = (1, 2, 3)
    tuple_2 = ("jack", 2, "tom", False)

    # 一个元组中如果有两个元素，我们就称之为二元组；一个元组中如果五个元素，我们就称之为五元组
    # ()表示空元组
    # 但是如果元组中只有一个元素，需要加上一个逗号

    a = ('java')  # <class 'str'>
    b = ('java',)  # <class 'tuple'>

    print(type(a))
    print(type(b))

    print(tuple_1)
    print(tuple_2)

    #  查看类型
    print(type(tuple_1))  # 输出：<class 'tuple'>

    #  查看元组中元素的数量
    print(len(tuple_2))

    #  索引运算
    print(tuple_2[2])

    # 切片
    print(tuple_2[1:4])  # 输出：(2, 'tom', False)

    # 遍历
    for index in tuple_2:
        print(index)

    # 拼接
    print(tuple_1 + tuple_2)  # 输出： (1, 2, 3, 'jack', 2, 'tom', False)

    # 打包和解包
    # 当我们把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型；
    # 当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量
    abc = 1, 2, 3
    print(type(abc))  # 输出:<class 'tuple'>

    i, j, k = abc  # 赋值变量和元组内的数量一致，不然会报错，变量少于元组内的元素数量报ValueError: too many values to unpack (expected 3)
    # 变量多于元组内的元素数量会报：ValueError: not enough values to unpack (expected 3, got 2)
    print(i, j, k)

    # 交换
    tuple_1, tuple_2 = tuple_2, tuple_1
    print(tuple_1)
    print(tuple_2)

    # 元组和列表转换
    print(list(tuple_1))
    print(tuple(list(tuple_1)))

    # 元组和列表的比较
    # 1、元组是不可变类型，不可变类型更适合多线程环
    # 2、不可变类型在创建时间上优于对应的可变类型


if __name__ == '__main__':
    tuple_test()
