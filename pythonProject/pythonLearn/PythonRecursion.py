#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示

def fact(n) :
    if n == 1 :
        return 1
    return n * fact(n - 1);

print(fact(1))
print(fact(5))
print(fact(10))

# 计算fact(5)的过程
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120

# 尾递归

def fact2(n) :
    return fact_item(n, 1)

def fact_item(num, product) :
    if num == 1 :
        return product
    return fact_item(num - 1, num * product)

# 汉诺塔

def move(n,a,b,c):
    if n == 0:
        return
    elif n == 1:
        print(a,"--->",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3,'A','B','C')