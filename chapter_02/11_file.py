#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2026/2/4
# @Author  : fxmaoyuzzz
# @Software: PyCharm
# @File    : 11_file.py



# 用open函数打开文本文件时，需要指定文件名并将文件的操作模式设置为'r'，如果不指定，默认值也是'r'；
# 如果需要指定字符编码，可以传入encoding参数，如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码。

# 读写文本文件
def file_read():
    file = open('/Users/fxmaoyuzzz/workspace/读取文件.txt', 'r', encoding='utf-8')
    print(file.read())
    file.close()

    # 如果要向文件中写入内容，可以在打开文件时使用w或者a作为操作模式
    # 前者会截断之前的文本内容写入新的内容，后者是在原来内容的尾部追加新的内容。
    file = open('/Users/fxmaoyuzzz/workspace/读取文件.txt', 'a', encoding='utf-8')
    file.write('\n操作：《文件写入》')
    file.write('\n时间：2077年1月')
    file.close()

#     异常处理
def file_read_exception():
    file = None
    try:
        file = open('/Users/fxmaoyuzzz/workspace/读取文件1.txt', 'r', encoding='utf-8')
        print(file.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if file:
            file.close()

#   python内置异常：
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning


# 读写二进制文件

# 读写二进制文件跟读写文本文件的操作类似，在使用open函数打开文件时，
# 如果要进行读操作，操作模式是'rb'，如果要进行写操作，操作模式是'wb'。
# 读写文本文件时，read方法的返回值以及write方法的参数是str对象（字符串），
# 而读写二进制文件时，read方法的返回值以及write方法的参数是bytes-like对象（字节串）。
def file_read_rb():
    try:
        with open('/Users/fxmaoyuzzz/workspace/WechatIMG153.jpeg', 'rb') as file1:
            data = file1.read()
        with open('Aniya.jpg', 'wb') as file2:
            file2.write(data)
    except FileNotFoundError:
        print('指定的文件无法打开.')
    except IOError:
        print('读写文件时出现错误.')
    print('程序执行结束.')

# 如果要复制的图片文件很大，一次将文件内容直接读入内存中可能会造成非常大的内存开销，
# 为了减少对内存的占用，可以为read方法传入size参数来指定每次读取的字节数，
# 通过循环读取和写入的方式来完成上面的操作
def file_read_rb_szie():
    try:
        with open('/Users/fxmaoyuzzz/workspace/WechatIMG153.jpeg.jpg', 'rb') as file1, open('Aniya.jpg', 'wb') as file2:
            data = file1.read(512)
            while data:
                file2.write(data)
                data = file1.read()
    except FileNotFoundError:
        print('指定的文件无法打开.')
    except IOError:
        print('读写文件时出现错误.')
    print('程序执行结束.')

if __name__ == '__main__':
    # file_read()
    file_read_rb_szie()