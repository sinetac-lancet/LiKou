# -*- coding: utf-8 -*-
# @Time  : 2023/04/11 22:43
# @author: dtf

# https://dream.blog.csdn.net/article/details/129216271


money = int(input())
price = list(map(int, input().split()))
price.sort()
print(money)
print(price)

n = len(price)

if money <= n:
    print(price[money-1])
else:
    m = money - n
    print(price[-1] + price[m-1])



