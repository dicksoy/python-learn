#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 生成1-10
print(list(range(1, 11)))

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L=[]
for x in range(1, 11) :
    L.append(x * x)
print(L)

# 用一行语句代替循环生成上面的list
print([x * x for x in range(1, 11)])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])

# 使用两层循环，可以生成全排列(三层和三层以上的循环就很少用到了)
print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': "A", "y": "B", "z": "C"}
for k,v in d.items() :
    print(k, "=", v)

# 因此，列表生成式也可以使用两个变量来生成list
d1 = {'x': "A", "y": "B", "z": "C"}
print([k + "=" + v for k, v in d1.items()])

# 最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])