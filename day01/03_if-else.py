#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/1/23
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : 03_if-else.py

# if-else 结构

def bmi_test():
    height = float(input('身高(cm)：'))
    weight = float(input('体重(kg)：'))
    bmi = weight / (height / 100) ** 2
    print(f'{bmi = :.1f}')
    if 18.5 <= bmi < 24:
        print('你的身材很曼妙！')
    else:
        print('你的身材不太妙！')


# for循环

import time

def time_for():
    for i in range(3600):
        print('hello, world')
        time.sleep(1)

# while循环
def while_test():
    i = 0;
    total = 0;
    while (i <= 100):
        total += i;
        i += 1;
    print(total)


# break和 continue
def break_test():
    i = 0;
    total = 0;
    while True:
        total += i;
        i += 1;
        if i > 100:
            print(total)
            break
        else:
            print("继续" + str(i))
            continue;


#


if __name__ == '__main__':
    break_test()




