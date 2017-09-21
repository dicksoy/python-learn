#!/usr/bin/python
# -*- coding: UTF-8 -*-

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 4, 5, 6)
print(f)    # 此时输出的不是求和结果，而是求和函数
print(f())  # 调用函数f，才是真正的求和结果