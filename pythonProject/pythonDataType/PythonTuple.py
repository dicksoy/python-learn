#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python元组
# 元组是另一个数据类型，类似于List（列表）。
# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

tuple = ('dicksoy', 123, 2.33);
tinytuple = (123, 'Join');

print tuple;
print tuple[0];
print tuple[0:2];
print tuple[2:];
print tinytuple * 2;
print tuple + tinytuple;

# tuple[2] = 1000;  元组不能修改
print tuple;