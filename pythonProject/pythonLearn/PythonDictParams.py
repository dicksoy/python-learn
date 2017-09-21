#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def person(name, age, **kw) :
    print ("name :", name, " age :", age, " other :", kw)

def kyTest(name, age, *args, city, job) :
    print(name, age, args, city, job)


person("dicksoy", 30)
person("dicksoy", 20, city="Beijing", test="123")

kyTest("dicksoy", 20, city="haha", job="zhangsan")