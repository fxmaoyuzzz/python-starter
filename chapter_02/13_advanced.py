#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/2/4
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : 13_advanced.py


# 生成式（推导式）的用法
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}


# 用股票价格大于100元的股票构造一个新的字典
def new_price():
    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)  # {'AAPL': 191.88, 'GOOG': 1186.96, 'IBM': 149.24, 'ACN': 166.89, 'FB': 208.09}


def list_two():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    # 录入五个学生三门课程的成绩
    # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
    # 第一种写法创建的是「浅拷贝」的二维列表，所有行都指向同一个底层列表对象
    # Python中可变对象（列表、字典等）的乘法/直接赋值是浅拷贝，仅复制引用，而非创建新对象；而列表推导式会为每次循环生成新对象。
    # scores = [[None] * len(courses)] * len(names)
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
            print(scores)


def heapq():
    import heapq

    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


def itertools():
    import itertools

    # 产生ABCD的全排列
    print(list(itertools.permutations('ABCD')))
    # 产生ABCDE的五选三组合
    print(list(itertools.combinations('ABCDE', 3)))
    # 产生ABCD和123的笛卡尔积
    print(list(itertools.product('ABCD', '123')))
    # 产生ABC的无限循环序列
    print(list(itertools.cycle(('A', 'B', 'C'))))


# collections模块
# namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。
# deque：双端队列，是列表的替代实现。Python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和删除元素时，deque会表现出更好的性能，渐近时间复杂度为$O(1)$。
# Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素。Counter和dict的继承关系我认为是值得商榷的，按照CARP原则，Counter跟dict的关系应该设计为关联关系更为合理。
# OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为。
# defaultdict：类似于字典类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法更加高效。
def collections():
    from collections import Counter

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter.most_common(3))


if __name__ == '__main__':
    collections()
