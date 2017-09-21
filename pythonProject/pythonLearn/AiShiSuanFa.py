#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 埃氏算法

# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
# 注意这是一个生成器，并且是一个无限序列。
def _odd_iter() :
    n = 1
    while True :
        n = n + 2
        yield n

# 然后定义一个筛选函数：
def _not_divisible(n) :
    return lambda x: x % n > 0

# 最后，定义一个生成器，不断返回下一个素数：
def primes() :
    yield 2
    it = _odd_iter()    # 初始序列
    while True :
        n = next(it)    # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列

for n in primes() :
    if n < 10 :
        print(n)
    else:
        break