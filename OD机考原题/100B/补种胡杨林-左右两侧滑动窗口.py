# -*- coding: utf-8 -*-
# @Time  : 2023/05/21 17:17
# @author: dtf

# https://dream.blog.csdn.net/article/details/129678220
'''
求，可以得到最多连续的胡杨林

N 总种植数量
M 未成活数量
未成活数目位置
K 最多可补种数量

示例1：
10
3
2 4 7
1

输出：6

'''


nn = int(input())
mm = int(input())
data = list(map(int, input().split()))
kk = int(input())

dp = [0] * nn
for i in range(mm):
    dp[int(data[i]) - 1] = 1

left, right = 0, 0
count = 0
res = 0
while right < nn:
    while right < nn and count <= kk:
        if dp[right] == 1:
            count += 1
        right += 1

        if count <= kk:
            res = max(res, right - left)    # ！！！注意right - left

    while left <= right and count > kk:
        if dp[left] == 1:
            count -= 1
        left += 1

print(res)
