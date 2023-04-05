# -*- coding: utf-8 -*-
# @Time  : 2023/04/05 16:02
# @author: dtf

# https://dream.blog.csdn.net/article/details/129432504
'''
所谓质数或称素数，就是一个正整数，除了本身和 1 以外并没有任何其他因子。例如 2，3，5，7 是质数，而 4，6，8，9 则不是，后者称为合成数。

一、核心点：
从2 到 number 的平方根范围内枚举所有可能的因子i，如果i 可以被 number整除，则将number 分解 i和number//i 两个数的积，然后判断
i和number//i是否都是质数。如果都是质数，则输出 i和number//i 并退出程序；否则继续枚举。

二、思路分析
1、为什么要在2~number平方根的范围查找？
答：举例 num 被4整除，还是被16整除 结果是一样的
'''
import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:  # 判断x是否除了1和自身外，还能被其他数字整除
            return False
    return True


num = int(input())
# 质数，就是一个整数，除了本身和1以外并没有任何其他因子
for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:    # 是否能被 i 整除
        if is_prime(i) and is_prime(num//i):    # 是否能被 num//i 整除
            # num = i * (num//i)
            print(i, num//i)
            exit()

print('NO')




