# -*- coding: utf-8 -*-
# @Time  : 2023/04/02 16:27
# @author: dtf


# https://dream.blog.csdn.net/article/details/129233148


'''
个人思考：
统计干货总数量gh、湿货总数量sh ==>最大值_max
单类中转车数量nc

_mean = _max // nc

max(供应商货物信息)


'''

import sys

goods_num = int(input())
gh_info = list(map(int, input().split()))
hw_info = list(map(int, input().split()))
car_num = int(input())

# data = zip(gh_info, hw_info)
gh, sh = [], []
for i, j in zip(gh_info, hw_info):
    if j == 0:
        gh.append(i)
    else:
        sh.append(i)
_max = max(len(gh), len(sh))
gh_max = max(gh)
sh_max = max(sh)
_mean = _max // goods_num

