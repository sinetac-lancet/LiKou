# -*- coding: utf-8 -*-
# @Time  : 2023/04/08 14:51
# @author: dtf

# https://dream.blog.csdn.net/article/details/129167547

'''
解题思路：充电设备组合 与 充电站最大功率比较

'''

N = int(input())
val = list(map(int, input().split()))
max_val = int(input())
val.sort()
print(val)

i = 0
while i < N:
    target = max_val - val[i]
    if target < 0:
        print(0)
        break
    j = i + 1
    while j < N and (0 < target < max_val):
        # print('target = ', target)
        if target in val[j:-1]:
            print(max_val)
            exit()
        target = target - val[j]
        j += 1
        # print('j = ', j)
    i += 1
    # print('i = ', i)
print(0)

'''
网页答案：动态规划
'''

# def solve_method(n, p, p_max):
#     dp = [[0] * (p_max + 1) for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         for j in range(1, p_max + 1):
#             if p[i - 1] > j:
#                 dp[i][j] = dp[i - 1][j]
#             else:
#                 dp[i][j] = max(dp[i - 1][j], p[i - 1] + dp[i - 1][j - p[i - 1]])
#
#     return dp[n][p_max]
#
# n = int(input())
# p = [int(x) for x in input().split()]
# p_max = int(input())
# print(solve_method(n, p, p_max))




