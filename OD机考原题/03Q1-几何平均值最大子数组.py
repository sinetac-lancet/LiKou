# -*- coding: utf-8 -*-
# @Time  : 2023/04/15 16:17
# @author: dtf


'''

题目理解：
第一行输入N、L，N表示number的大小（1<=N<=10000）,L表示子数组的最大长度（1<=L<=N）
之后行表示 number中的N个数
例如：
3 2
2
2
3
即，数组为[2, 2, 3]。查找几何平均数为最大的子数组的最小长度
'''

'''
思路：
按照指定的子数组长度L，得到所有的子数组
'''
import copy
import math
from collections import defaultdict

def calculate_mean(arr):
    res = 1
    for i in arr:
        res *= i
    return math.pow(res, 1/len(arr))


N, L = tuple(map(int, input().split()))
lst = []
for i in range(N):
    tmp = float(input())
    lst.append(tmp)
print(N, L, lst)

if N < L:
    print(0, 0)
    exit()

# 获取所有的子数组，根据大小排序，获取满足要求的子数组
# sub_dict = {}
# for i in range(N):
#     cnt = []
#     # sub_dict[str(lst[i])] = sub_dict.get(str(lst[i]), 0) + 1
#     for j in range(i, N):
#         cnt.append(lst[j])
#         sub_dict[str(cnt)] = sub_dict.get(str(cnt), 0) + 1
# print(sub_dict)

# sub_lst = []
# for i in range(N):
#     cnt = []
#     for j in range(i, N):
#         cnt.append(lst[j])
#         print(cnt)
#         if len(cnt) >= L:
#             sub_lst.append(copy.deepcopy(cnt))
# print(sub_lst)

sub_dict = defaultdict(list)
for i in range(N):
    cnt = []
    for j in range(i, N):
        cnt.append(lst[j])
        print(cnt)
        if len(cnt) >= L:
            cal_mean = calculate_mean(cnt)
            sub_dict[cal_mean].append(cnt)
print(sub_dict)