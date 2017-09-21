#!/usr/bin/python
# -*- coding: UTF-8 -*-

#   +     加 - 两个对象相加
#   -     减 - 得到负数或是一个数减去另一个数
#   *     乘 - 两个数相乘或是返回一个被重复若干次的字符串
#   /     除 - x除以y
#   %     取模 - 返回除法的余数
#   **    幂 - 返回x的y次幂
#   //    取整除 - 返回商的整数部分

a = 21;
b = 22;
c = 0;

c = a + b
print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c

c = a * b
print "3 - c 的值为：", c

c = a / b
print "4 - c 的值为：", c

c = a % b
print "5 - c 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print "6 - c 的值为：", c

a = 10
b = 5
c = a // b
print "7 - c 的值为：", c