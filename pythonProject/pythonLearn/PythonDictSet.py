#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 1、方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，
# 这种查找速度都非常快，不会随着字典大小的增加而变慢。

# 2、dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，
# 也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。

dict = {"test" : 123, "zhang" : 123123}
print dict.get("test1", -1) # 如果test1存在则返回值，否则返回-1
if "test" in dict :
    print dict["test"]
else :
    print dict["zhang"]

dict.pop("test")    # 删除1个key
print dict

# 无重复集合
s1 = set([1, 2, 3, 4, 5])
s2 = set([2, 4, 6])
s1.add(4)
s1.remove(4)
print s1 & s2   # 交集
print s2 | s1   # 并集