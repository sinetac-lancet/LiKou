# -*- coding: utf-8 -*-
# @Time  : 2023/04/05 15:40
# @author: dtf

# https://dream.blog.csdn.net/article/details/129600570
import sys


num = int(input())
data = []
for i in range(num):
    data.append(int(input()))
print(num, data)

data2 = list(set(data))
data3 = sorted(data2)
for i in data3:
    print(i)