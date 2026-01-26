#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/1/26
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : 09_function.py


# ===定义函数===

def function_name(agr1, agr2):
    return 'result'


# def：函数定义关键字
# function_name：函数名
# agr：参数
# return：返回关键字
# result：函数返回值

# ===函数的参数===

def function_1(a, b, c):
    return a + b + c


# 上述函数 function_1 函数有三个参数，这种参数叫做位置参数
# 在调用函数时通常按照从左到右的顺序依次传入
# 而且传入参数的数量必须和定义函数时参数的数量相同

# 如果不想按照从左到右的顺序依次给出a、b、c 三个参数的值
# 也可以使用关键字参数，通过“参数名=参数值”的形式为函数传入参数
# print(function_1(b=2, c=3, a=1))
# print(function_1(c=6, b=4, a=5))

# ==强制位置参数==

def function_2(a, b, c, /):
    return a + b + c;


# 上述函数function_2中'/'前面的参数是强制位置参数
# 调用该函数时必须按照参数位置顺序来接收参数值
# 下面的传参方式是错误的，会报：TypeError: function_2() got some positional-only arguments passed as keyword arguments: 'a, b, c'
# print(function_2(b=2, c=3, a=1))

# print(function_3(3,2,1)) 会报：TypeError: function_3() takes 0 positional arguments but 3 were given


# ==命名关键字参数==
def function_3(*, a, b, c):
    return a + b + c;


# '*'后面的参数是命名关键字参数
# '*'右侧的所有参数（a、b、c）必须显示通过像a=xxx、b=xxx、c=xxx这样传递
# a、b、c 的传递顺序不要求和定义顺序一致，只要参数名正确即可
# a、b、c 都是必选参数（没有默认值），调用时不能少传


# ==参数默认值==
def add(a=0, b=0, c=0):
    return a + b + c


# 上述 add 函数的三个参数a、b、c默认值都是 0
# 调用add函数，没有传入参数，会使用默认值0
# print(add())         # 输出：0
# 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
# print(add(1))        # 输出：1
# 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
# print(add(1, 2))     # 输出：3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
# print(add(1, 2, 3))  # 输出：6

# 带默认值的参数必须放在不带默认值的参数之后
# def add_1(a=0, b, c=0):
#     return a + b + c
# 上述函数会提示错误：non-default parameter follows default parameter


# ==可变参数==
# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())         # 0
print(add(1))        # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.45


# 如果希望通过“参数名=参数值”的形式传入若干个参数，具体有多少个参数也不确定
# 还可以给函数添加【可变关键字参数】，传入的关键字参数会组装到一个字典中

# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)

# 输出：(3, 2.1, True) {'name': '骆昊', 'age': 43, 'gpa': 4.95}

# 在进行 import 导入函数时，如果从两个不同的模块中导入了同名的函数，后导入的函数会替换掉之前的导入
# 因此要避免同名，或者使用 as 关键字对导入的函数进行别名


# Python 标准库中还有一类函数是不需要import就能够直接使用的，称之为内置函数
# 一些内置函数：
# abs：返回一个数的绝对值，例如：abs(-1.3)会返回1.3。
# bin：把一个整数转换成以'0b'开头的二进制字符串，例如：bin(123)会返回'0b1111011'。
# chr：将Unicode编码转换成对应的字符，例如：chr(8364)会返回'€'。
# hex：将一个整数转换成以'0x'开头的十六进制字符串，例如：hex(123)会返回'0x7b'。
# input：从输入中读取一行，返回读到的字符串。
# len：获取字符串、列表等的长度。
# max：返回多个参数或一个可迭代对象中的最大值，例如：max(12, 95, 37)会返回95。
# min：返回多个参数或一个可迭代对象中的最小值，例如：min(12, 95, 37)会返回12。
# oct：把一个整数转换成以'0o'开头的八进制字符串，例如：oct(123)会返回'0o173'。
# open：打开一个文件并返回文件对象。
# ord：将字符转换成对应的Unicode编码，例如：ord('€')会返回8364。
# pow：求幂运算，例如：pow(2, 3)会返回8；pow(2, 0.5)会返回1.4142135623730951。
# print：打印输出。
# range：构造一个范围序列，例如：range(100)会产生0到99的整数序列。
# round：按照指定的精度对数值进行四舍五入，例如：round(1.23456, 4)会返回1.2346。
# sum：对一个序列中的项从左到右进行求和运算，例如：sum(range(1, 101))会返回5050。
# type：返回对象的类型，例如：type(10)会返回int；而 type('hello')会返回str。




if __name__ == '__main__':
    # print(function_2(b=2, c=3, a=1))
    print(function_3(3, 2, 1))
