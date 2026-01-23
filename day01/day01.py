#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/1/22
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : day01.py


# 变量
if __name__ == '__main__':
    # print(100)  # 整型（int）
    # print(123.456)  # 浮点型（float）
    # print("python")  # 字符串
    # print(True)  # bool 型
    a = 100
    b = 123.45
    c = '123'
    d = '100'
    e = '123.45'
    f = 'hello, world'
    g = True
    print(float(a))  # int类型的100转成float，输出100.0
    print(int(b))  # float类型的123.45转成int，输出123
    print(int(c))  # str类型的'123'转成int，输出123
    print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
    print(int(d, base=2))  # str类型的'100'按二进制转成int，输出4

    # str类型转int类型时可以通过base参数来指定进制，可以将字符串视为对应进制的整数进行转换。
    # str类型转成bool类型时，只要字符串有内容，不是''或""，对应的布尔值都是True。
    # bool类型转int类型时，True会变成1，False会变成0。
    # 在 ASCII 字符集和 Unicode 字符集中， 字符'd'对应的编码都是100。

    print(float(e))  # str类型的'123.45'转成float，输出123.45
    print(bool(f))  # str类型的'hello, world'转成bool，输出True
    print(int(g))  # bool类型的True转成int，输出1
    print(chr(a))  # int类型的100转成str，输出'd'
    print(ord('d'))  # str类型的'd'转成int，输出100


#     变量命名规则
# 1、变量名由字母、数字和下划线构成，数字不能开头
#     惯例1：变量名通常使用小写英文字母，多个单词用下划线进行连接。
#     惯例2：受保护的变量用单个下划线开头。
#     惯例3：私有的变量用两个下划线开头。
# 2、大小写敏感
# 3、尽可能避开 Python 的保留字

