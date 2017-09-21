#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 装饰器模式

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2017-09-20')

print(now())

