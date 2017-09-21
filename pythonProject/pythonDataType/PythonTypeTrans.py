#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python数据类型转换

# int() 函数用于将一个字符串会数字转换为整型。
print int('12', 16);    # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
print int('0xa', 16);
# 语法：class int(x, base=10)
# x -- 字符串或数字。
# base -- 进制数，默认十进制。

# long() 函数将数字或字符串转换为一个长整型。
print long('1');
# 语法：class long(x, base=10)
# x -- 字符串或数字。
# base -- 可选，进制数，默认十进制。

# float() 函数用于将整数和字符串转换成浮点数。
print float(111);
print float('222');
# 语法：class float([x])
# x -- 整数或字符串

# complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
print complex(1, 2);
print complex("1+2j");  # 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
# 语法：class complex([real[, imag]])
# real -- int, long, float或字符串；
# imag -- int, long, float；

# str() 函数将对象转化为适于人阅读的形式。
print str(123456);
dict = {'name':'dicksoy','test':"demo"};
print str(dict);
# 语法：class str(object='')
# object -- 对象。

# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
print eval("3 * 2");
print eval('pow(2,2)')
# 语法：eval(expression[, globals[, locals]])
# expression -- 表达式。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

# Python 元组 tuple() 函数将列表转换为元组。
print tuple([1,2,3,4]);
print tuple({1:2,3:4}); # 针对字典 会返回字典的key组成的tuple
print tuple((1,2,3,4)); #元组会返回元组自身
# 语法：tuple( seq )
# seq -- 要转换为元组的序列。

# list() 方法用于将元组转换为列表。
# 注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
aTuple = (123, "xml", 'abc');
aList = list(aTuple);
print aList;
# 语法：list( seq )
# list -- 要转换为列表的元组。

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
x = set("dicksoy");
y = set("change soy");
print x,y # 重复的被删除
# set(['c', 'd', 'i', 'k', 'o', 's', 'y']) set(['a', ' ', 'c', 'e', 'g', 'h', 'o', 'n', 's', 'y'])
print x & y   # 交集
# set(['y', 'c', 's', 'o'])
print x | y   # 并集
# set(['a', ' ', 'c', 'e', 'd', 'g', 'i', 'h', 'k', 'o', 'n', 's', 'y'])
print x - y   # 差集
# set(['i', 'k', 'd'])
# 语法：class set([iterable])
# iterable -- 可迭代对象对象；

# ************************************************* 报错 *************************************************************
# dict() 函数用于创建一个字典。
# dictValue = dict(); # 创建空字典
# dict(a="a", b="b", t="t");  # 传入关键字
# dict(zip(['one', 'two', 'three'], [1, 2, 3]));  # 映射函数方式来构造字典
# dict([('one', 1), ('two', 2), ('three', 3)]);   # 可迭代对象方式来构造字典
# 语法：class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# **kwargs -- 关键字
# mapping -- 元素的容器。
# iterable -- 可迭代对象。
# ************************************************* 报错 *************************************************************

# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
a = frozenset(range(10))     # 生成一个新的不可变集合
print a;
b = frozenset('runoob');    # 创建不可变集合
print b;
# 语法：class frozenset([iterable])
# iterable -- 可迭代的对象，比如列表、字典、元组等等。

# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
print chr(0x30), chr(0x31), chr(0x61)   # 十六进制
print chr(48), chr(49), chr(97)         # 十进制
# 语法：chr(i)
# i -- 可以是10进制也可以是16进制的形式的数字。

# unichr() 函数 和 chr()函数功能基本一样， 只不过是返回 unicode 的字符。
print unichr(97);
print unichr(98);
print unichr(99);
# 语法：unichr(i)
# i -- 可以是10进制也可以是16进制的形式的数字。

# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
# 如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
print ord("a");
print ord("b");
# 语法：ord(c)
# c -- 字符。

# hex() 函数用于将10进制整数转换成16进制整数。
print hex(255);
print hex(-42);
# 语法：hex(x)
# x -- 10进制整数

# oct() 函数将一个整数转换成8进制字符串。
print oct(255);
print oct(-20);
# 语法：oct(x)