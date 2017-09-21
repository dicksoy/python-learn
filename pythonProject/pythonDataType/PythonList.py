#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python列表

# 加号 + 是列表连接运算符，星号 * 是重复操作

list = ['runnoob', 765, 2.33, 'dicksoy', 89.0];
tinyList = [123, 'John'];

print list;                 # 输出完整列表
print list[0];              # 输出第一个元素
print list[0:3];            # 输出第1-3个元素
print list[2:];             # 第3个开始输出
print tinyList * 2;         # 输出2次
print list + tinyList;      # 输出组合列表