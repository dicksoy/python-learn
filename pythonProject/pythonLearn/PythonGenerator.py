#!/usr/bin/python
# -*- coding: UTF-8 -*-

# list
L = [x * x for x in range(10)]
print(L)

# generator
g = (x * x for x in range(10))
print(g)
print(next(g))  # 通过next()函数获得generator的下一个返回值

for n in g :
    print(n)