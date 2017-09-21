#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 绝对值
print abs(100)
print abs(-20)
print abs(12.34)

# 返回最大的值
print max(1, 2, 9, 100)
print max(1, 99)

# 数据类型转换
print int('123')
print int(12.34)
print str('1.23')
print bool(1)
print bool('')

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print a(-1)

# 定义函数
def my_abs(x) :
    if not isinstance(x, (int, float)) :
        raise TypeError("bad operand type")
    if x >= 0 :
        return x
    else :
        return -x

print "自定义函数my_abs :", my_abs(-928)
# return None可以简写为return

# 空函数
def nop():
    pass
