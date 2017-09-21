#!/usr/bin/python
# -*- coding: UTF-8 -*-

def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))

print('asdfghjk'[::-1])