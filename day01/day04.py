#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/1/23
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : day04.py


# list：列表是由一系元素按特定顺序构成的数据序列，可重复
def list_eg():
    list_1 = [1, 2, 3, 4, 5, 6, 7];
    list_2 = ['name', 'age', 'sex'];
    list_3 = [True, 1, 100.77, 'student'];
    list_4 = [1, 2, 7, 8];

    print(list_1);
    print(list_2);
    print(list_3);

    print(list_1 + list_2)  # 可以进行合并运算
    print(list_1 * 2)  # 将列表元素重复2遍，输出：[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]

    print(7 in list_1)  # 判断元素是否在列表中，输出：False
    print(7 in list_4)  # 判断元素是否在列表中，输出：True

    print(list_2[1])  # 取列表中下标为 1 的数据，索引从 0 开始，因此输出：age
    print(list_2[-3])  # 反向索引，[-1]可以访问列表中的最后一个元素，[-N]可以访问第一个元素，输出：name
    # print(list_2[4])  # 避免越界，否则会报错：IndexError: list index out of range

    list_3[3] = 'teacher'  # 对指定元素修改
    print(list_3)

    print(list_4[1:3])  # 切片，从列表位置 1 开始，取到位置 3（不包含位置 3 元素）
    print(list_4[:2])  # 开始位置是 0 的时候可以省略
    print(list_1[:5:2])  # 从开始位置取，取到第 5 个位置（不包含位置 5 元素），步长为 2（每隔两个取一个）

    print(list_1[-4:-1])
    print(list_1[-3::-1])  # 操作会获取从 list_1 的倒数第三个元素开始，以步长为 1 从后往前截取到序列开头的子序列，输出：[5, 4, 3, 2, 1]

    # 列表的遍历
    # 方式一：len函数可以获取列表元素的个数N，而range(N)则构成了从0到N-1的范围，刚好可以作为列表元素的索引
    for index in range(len(list_2)):
        print(list_2[index])

    # 方式二：直接对列表做循环，循环变量就是列表元素
    for index in list_2:
        print(index)


if __name__ == '__main__':
    list_eg()
