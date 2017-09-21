#!/usr/bin/python
# -*- coding: UTF-8 -*-

from collections import Iterable

d = {"a": 123, "b": 456, "c": 789, "d": 0}
for key in d :
    print(key)

for v in d.values() :
    print(v)

for k, v in d.items() :
    print(k,v)

# 判断是否可以迭代
print(isinstance(123, Iterable))
print(isinstance("BCASHD", Iterable))

# 下标循环
for i, v in enumerate(['A', 'B', 'C']) :
    print(i,v)

# 同时引用了两个变量，在Python里是很常见的
for x, y in [(1, 1), (2, 4), (3, 9)] :
    print(x,y)

