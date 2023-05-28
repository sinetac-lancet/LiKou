# -*- coding: utf-8 -*-
# @Time  : 2023/05/21 12:41
# @author: dtf
# https://blog.csdn.net/hihell/article/details/129067064

'''
太阳能板的安装面积受限于最短一侧的那根支柱的长度
先提供一组整型数组的支撑高度数据
假设每根支柱间的距离相等为一个单位长度
计算如何选择两根支柱可以使太阳能板的面积最大
输入：10，9，8，7，6，5，4，3，2，1
    注释：支柱至少为两根，最多为10000根
    柱子的高度是无序的
输出：可以支撑的最大太阳能板面积（10m高的支柱和5m高支柱之间）
    25
说明：10m与5m，之间间隔5，高度较小者为5，因此可以支撑最大面积为5*5
'''

import sys

data = list(map(int, input().split(',')))
# data.sort(reverse=True)
res = 0
for i in range(len(data)):
    total = 0
    for j in range(i+1, len(data)):
        min_val = min(data[i], data[j])
        total = (j - i) * min_val
        res = max(res, total)
print(int(res))
