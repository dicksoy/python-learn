#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python字典
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

dict = {};
dict['one'] = "this is one";
dict[2] = "this is two";

tinydict = {'name': 'dicksoy',
            'code':123,
            'dept':98.0,
            'list':[111,222]};
print dict['one'];
print dict[2];
print tinydict;
print tinydict.keys();
print tinydict.values();