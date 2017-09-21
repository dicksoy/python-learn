#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

# Python 返回值是一个tuple，但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值

def move(x, y, step, angle = 0) :
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y

r = move(100, 100, 60, math.pi / 6)
print r

def quadratic(a, b, c) :
    if not isinstance(a, (int,float)) :
        raise TypeError("type error");
    if not b ** 2 - 4 * a * c >= 0:
        return 'no value'
    else :
        x1 = (- b + math.sqrt(b * 2 - 4 * a * c)) / (2 * a)
        x2 = (- b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2

print quadratic(1,22,5);