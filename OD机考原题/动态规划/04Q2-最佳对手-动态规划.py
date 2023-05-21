# -*- coding: utf-8 -*-
# @Time  : 2023/05/08 19:33
# @author: dtf

# https://dream.blog.csdn.net/article/details/130557314


num, threshold = tuple(map(int, input().split()))
data = list(map(int, input().split()))
data.sort()
print(num, threshold)
print(data)
'''
动态规划会记录上一步的结果，因此最终的结果取最后一位即可
'''
dp = [0]*num
dp[0] = 0   # 自己和自己对比，差距为0
# 1、2位对比
if data[1] - data[0] <= threshold:
    dp[1] = data[1] - data[0]
else:
    dp[1] = 0
# 遍历剩余
for i in range(2, num):
    # dp[i]等于 前面的数据相加 + 自己和上一位的比较结果
    if data[i] - data[i-1] <= threshold:
        dp[i] = dp[i-2] + data[i] - data[i-1]
    else:
        dp[i] = dp[i-1]
print(dp)

# 等同于print(dp[-1]) if dp[-1] else print(-1)
if dp[num-1]:
    print(dp[num-1])
else:
    print(-1)







