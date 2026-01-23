#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/1/23
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : day07.py


# 集合

# 1、集合不允许重复元素
# 2、集合并不支持索引运算

# 集合中的元素必须是hashable类型，所谓hashable类型指的是能够计算出哈希码的数据类型，通常不可变类型都是hashable类型，
# 如整数（int）、浮点小数（float）、布尔值（bool）、字符串（str）、元组（tuple）等。
# 可变类型都不是hashable类型，因为可变类型无法计算出确定的哈希码，所以它们不能放到集合中。
# 例如：我们不能将列表作为集合中的元素；同理，由于集合本身也是可变类型，所以集合也不能作为集合中的元素。
# 我们可以创建出嵌套列表（列表的元素也是列表），但是我们不能创建出嵌套的集合。

def set_test():
    set_1 = {1, 2, 3, 4, 4, 5, 5}
    print(set_1)  # 输出：{1, 2, 3, 4, 5}

    # 遍历
    for index in set_1:
        print(index)

    # 集合的运算
    # 成员运算
    print(3 in set_1)  # True
    print(31 in set_1)  # False
    print(31 not in set_1)  # True

    # 二元运算（交集、并集、差集、对称差）
    set2 = {1, 2, 3, 4, 5, 6, 7}
    set3 = {2, 4, 6, 8, 10}
    # 交集
    print(set2 & set3)  # {2, 4, 6}
    print(set2.intersection(set3))  # {2, 4, 6}
    # 并集
    print(set2 | set3)  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
    print(set2.union(set3))  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
    # 差集
    print(set2 - set3)  # {1, 3, 5, 7}
    print(set2.difference(set3))  # {1, 3, 5, 7}
    # 对称差
    print(set2 ^ set3)  # {1, 3, 5, 7, 8, 10}
    print(set2.symmetric_difference(set3))  # {1, 3, 5, 7, 8, 10}

    # 比较运算
    set4 = {1, 2, 3}
    set5 = {1, 2, 3, 4, 5}
    set6 = {5, 4, 3, 2, 1}
    print(set4 < set5)  # True
    print(set4 <= set5)  # True
    print(set5 < set6)  # False
    print(set5 <= set6)  # True
    print(set5 == set6)  # True

    print(set4.issubset(set5))  # True，issubset判断是不是子集
    print(set5.issuperset(set4))  # True，issuperset判断是不是超集

    # 添加元素
    set4.add(7)
    print(set4)  # {1, 2, 3, 7}

    # 删除元素
    set4.discard(7)
    set4.discard(71)  # discard删除不存在的元素不会报错
    print(set4)  # {1, 2, 3}
    set4.remove(3)  # {1, 2}
    # set4.remove(31) # 如果要删除的元素不存在会报错：KeyError: 7
    # 因此使用 remove删除前，最好判断一下是否存在
    if 4 in set5:
        set5.remove(4)
        print(set5)  # {1, 2, 3, 5}

    # 清空元素
    set5.clear()
    print(set5)  # set()

    # 判断是否存在相同元素
    set6 = {'Java', 'Python', 'C++', 'Kotlin'}
    set7 = {'Kotlin', 'Swift', 'Java', 'Dart'}
    set8 = {'HTML', 'CSS', 'JavaScript'}
    print(set6.isdisjoint(set7))  # False
    print(set6.isdisjoint(set8))  # True

    # 不可变集合
    # 除了不能添加和删除元素，frozenset在其他方面跟set是一样的
    fset1 = frozenset({1, 2, 3, 4})
    # fset1.add(5) # AttributeError: 'frozenset' object has no attribute 'add'
    # fset1.discard(3) # AttributeError: 'frozenset' object has no attribute 'discard'
    # fset1.remove(3)  # AttributeError: 'frozenset' object has no attribute 'remove'
    print(fset1)


if __name__ == '__main__':
    set_test()
