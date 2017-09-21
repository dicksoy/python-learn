#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fib(max) :
    n, a, b = 0, 0, 1
    while n < max :
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'return';

# 把fib变成generator

def fibGenerator(max) :
    n, a, b = 0, 0, 1
    while n < max :
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done';

print(fib(10))
print(next(fibGenerator(3)))
# 测试执行顺序
def odd() :
    print("test 1")
    yield 1
    print("test 2")
    yield 3
    print("test 3")
    yield 5

o = odd()
print(next(o))
print(next(o))

from collections import Iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
