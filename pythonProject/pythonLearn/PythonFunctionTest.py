#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 位置参数
def power(x, n) :
    s = 1
    while n > 0 :
        n = n - 1
        s = s * x
    return s

print(power(5, 2))
print(power(15, 3))

# 默认参数

def power2(x, n=2) :
    s = 1
    while n > 0 :
        n = n - 1
        s = s * x
    return s

print(power2(5))
print(power2(5, 3))

# 这样会出现错误，默认参数必须指向不变对象
def add_end(L=[]) :
    L.append('end')
    return L
print(add_end())
print(add_end())
print(add_end())
# 修改后的add_end
def add_end2(L=None) :
    if L is None :
        L = []
    L.append('end')
    return L;
print(add_end2())
print(add_end2())
print(add_end2())

# 可变参数
def calc(number) :
    sum = 0
    for n in  number :
        sum = sum + n * n
    return sum
print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))

def calc2(*numbers) :
    sum = 0
    for n in  numbers :
        sum = sum + n * n
    return sum

print(calc2(1, 2, 3))
print(calc2(1, 3, 5, 7))
nums = [1, 2, 3]
print(calc2(*nums))

# 关键字参数
def person(name, age, **kw) :
    print("name :", name, " age :", age, " other :", kw)

person('Michael', 30)
person('Bob', 35, city="BeiJing", address="东城区")
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
# 简化写法
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 命名关键字参数
def person2(name, age, *, city="北京", job) :
    print(name, age, city, job)

# 传入参数名，调用将报错
person2("diu", 25, city="beijing", job="colck")
person2("diu", 25, job="colck")

# 参数组合

def f1(a, b, c=0, *args, **kw) :
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw) :
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


