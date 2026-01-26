#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/1/23
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : 04_list.py


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

    # 追加元素
    list_2.append("add")
    print(list_2)
    # 指定位置插入元素
    list_2.insert(4, "insert")  # 输出：['name', 'age', 'sex', 'add', 'insert']
    print(list_2)

    list_2.insert(2, "index")  # 输出：['name', 'age', 'index', 'sex', 'add', 'insert']
    print(list_2)

    # 列表的append方法向列表中追加元素，将元素添加到列表的末尾；
    # 使用insert方法向列表中插入元素，而插入则是在指定的位置添加新元素（并不是覆盖原有位置上的元素，而是将插入位置及后面的元素后移一位）

    # 删除元素
    list_2.append("name")
    list_2.insert(3, "name")
    print("删除")
    print(list_2)
    list_2.remove("name")  # 如果所删除的元素不存在会报ValueError: list.remove(x): x not in list
    print(list_2)  # 如果列表中有多个值为 name 的元素，默认删除第一个

    list_2.pop()  # pop方法默认删除列表中的最后一个元素
    print(list_2)

    list_2.pop(2)  # pop方法也可以指定所删除的位置，但如果超出索引长度会报IndexError: pop index out of range
    print(list_2)

    # del关键字后面跟要删除的元素，这种做法跟使用pop方法指定索引删除元素没有实质性的区别，
    # 但pop会返回删除的元素，del在性能上略优，因为del对应的底层字节码指令是DELETE_SUBSCR，而pop对应的底层字节码指令是CALL_METHOD和POP_TOP
    print('del')
    del list_2[3]
    print(list_2)

    print(list_4)
    list_4.clear()  # 清空列表元素
    print(list_4)

    # 索引元素
    print(list_2.index("sex"))  # index方法可以查找某个元素在列表中的索引位置，如果找不到指定的元素，index方法会引发ValueError: 'sex1' is not in list

    # 排序
    list_2.sort()
    print(list_2)  # 输出：['age', 'index', 'insert', 'sex']

    # 反转
    list_2.reverse()
    print(list_2)  # 输出：['sex', 'insert', 'index', 'age']

    #  嵌套列表
    scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
    print(scores)

if __name__ == '__main__':
    list_eg()
