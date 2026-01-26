#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/1/23
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : 06_str.py


# 字符串
def str_test():
    str_1 = 'hello world !'
    print(str_1)

    # 转义
    str_2 = '\"hello world !\"'
    str_3 = '\\"hello world !\\"'
    print(str_2)  # 输出："hello world !"
    print(str_3)  # 输出：\"hello world !\"

    # \t、\r和\n都是转义字符，\t是制表符，\n是换行符，\r是回车符
    s1 = '\it \is \time \to \read \now'
    # 以 r 开头之后为原始字符串，意思是字符串中的每个字符都是它本来的含义，没有所谓的转义字符
    s2 = r'\it \is \time \to \read \now'
    print(s1)
    print(s2)  # 输出：\it \is \time \to \read \now

    # 字符运算
    s3 = 'hello'
    s4 = 'world'
    print(s3 + '-' + s4)  # 输出：hello-world

    s5 = '&' * 3
    print(s5)  # 输出：&&&

    s3 += s4
    print(s3)  # 输出：helloworld

    s3 *= 2
    print(s3)  # 输出：helloworldhelloworld

    tr1 = 'python'
    tr2 = 'python is good'
    tr3 = 'pythoa'

    print(tr1 == tr2)  # False
    print(tr1 == 'python')  # True
    print(tr1 < tr2)  # True
    print(tr1 < tr3)  # False
    print(ord('n'))  # 110
    print(ord('a'))  # 97
    # 比较运算：先逐字符比 Unicode 编码，当「短串是长串的完整前缀」（所有对应字符的 Unicode 都相同）时，会触发「前缀规则」
    # 比如上述的 tr1 是 tr2 的完整前缀，因此 tr1 < tr2
    # 逐字符对比时，找到任意一个位置的字符不同，就会停在该位置，直接比较这两个字符的 Unicode 编码，后续字符和长度都不再考虑，因此 tr1 < tr3 是 False

    # 成员运算
    print('good' in tr2)  # True
    print('good1' in tr2)  # False
    print('good' not in tr2)  # False

    # 获取长度
    print(len(tr3))

    # 索引和切片
    tr4 = 'abcdefg'
    print(tr4[1])  # b
    print(tr4[3])  # d
    print(tr4[2:5])  # 输出：cde

    # 遍历
    for index in range(len(tr4)):
        print(tr4[index])

    for index in tr4:
        print(index)

    # 字符串的方法
    tr5 = 'hello，world!'
    tr6 = 'HELLO，WORLD!'
    print(tr5.capitalize())  # 将首字母大写：Hello，world!
    print(tr5.title())  # 每个单词的首字母大写：Hello，World!
    print(tr5.upper())  # 整个字符串大写：HELLO，WORLD!
    print(tr6.lower())  # 整个字符串小写：hello，world!

    print(tr5)
    print(tr6)  # 由于字符串是不可变类型，使用字符串的方法对字符串进行操作会产生新的字符串，原来变量的值并没有发生变化。
    # 所以上面的代码中，当我们最后检查tr5和tr6两个变量的值时，tr5和tr6的值并没有发生变化

    # 查找
    print('ll' in tr5)  # True
    print('lls' in tr5)  # False

    print(tr5.find('ll'))  # 2
    print(tr5.find('lls'))  # -1，不到指定的字符串会返回-1

    print(tr5.index('ll'))  # 2
    # print(tr5.index('lls')) # ValueError: substring not found

    tr7 = 'abcdefg'
    tr8 = 'abcdefg12345'
    tr9 = 'abcdefg12345!'
    print(tr7.startswith('abc'))  # True
    print(tr7.startswith('abcf'))  # False
    print(tr7.endswith('efg'))  # True
    print(tr7.endswith('abc'))  # False

    print(tr8.isdigit())  # False, isdigit用来判断字符串是不是完全由数字构成的
    print(tr8.isalpha())  # False, isalpha用来判断字符串是不是完全由字母构成的
    print(tr8.isalnum())  # True, isalnum用来判断字符串是不是由字母和数字构成的
    print(tr9.isalnum())  # False

    # 格式化
    tr10 = 'hello world'
    print(tr10.center(20, '*'))  # ****hello world*****
    print(tr10.ljust(20))  # hello world
    print(tr10.rjust(20))  # hello world
    # ljust 和  rjust 用空格补齐，或者指定字符补齐
    print(tr10.ljust(20, '#'))  # hello world#########
    # 如果要在字符串的左侧补零，也可以使用zfill方法
    print(tr10.zfill(15))  # 0000hello world

    # 打印时格式化
    num_1 = 33
    num_2 = 2
    print(f'{num_1}*{num_2} = {num_1 * num_2}')  # 33*2 = 66

    # 修剪
    email = '   fxmaoyuzzz@aaa.com   '
    print(email)
    print(email.strip())  # strip方法去掉两端空格
    s10 = '@@python##'
    print(s10.lstrip('@'))  # python##
    print(s10.rstrip('#'))  # @@python

    # 替换
    print(s10.replace('@', '&'))  # &&python##
    print(s10.replace('@', '&', 1))  # &@python##，指定变更数量

    s11 = 'abc,de,f'
    spilt = s11.split(',')  # split方法默认使用空格进行拆分，也可以按照指定字符拆分
    print(spilt)  # ['abc', 'de', 'f']

    print('-'.join(spilt))  # abc-de-f，按照指定字符连接




if __name__ == '__main__':
    str_test()
