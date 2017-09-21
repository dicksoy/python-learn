#!/usr/bin/python
# -*- coding: UTF-8 -*-

names = ['Michael', 'Bob', 'Tracy']
for name in  names :
    print name

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] :
    sum = sum + x
print sum

# range(101)就可以生成0-100的整数
print range(101)
sum2 = 0
for x2 in range(101) :
    sum2 = sum2 + x2
print sum2

list2 = ['duc', 'dickisk', 'dicksoy']
for n in  list2 :
    print "hello ", n

n = 10
while n > 0 :
    n -= 1
    print n