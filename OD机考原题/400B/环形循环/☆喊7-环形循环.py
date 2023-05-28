# -*- coding: utf-8 -*-
# @Time  : 2023/05/21 20:50
# @author: dtf
# https://dream.blog.csdn.net/article/details/129052749
'''
N个人围成一圈，按顺时针从1-7编号
编号1的人从1开始喊数，
下一个喊得数字是上一个数字的+1
不能喊7或者包含7，要喊过

现给定一个长度N的数组，存储打乱的每个人喊过的次数
请把它还原成正切的顺序
即，数组的第i个元素存储编号i的人喊‘过’的次数

输入：
    输入一行 喊过的次数
    例如：0 1 0
输出：
    输出一行 顺序正确的喊过的次数
    例如：1 0 0
说明：
    只有1次过，发生在7
    按顺序编号1的人遇到7，所以1 0 0
    结束时的k不一定是7，也可以是8 9
    喊过都是 1 0 0

'''

'''
题目理解：
不能喊7或者包含7，例如 7、14、17、21、27、28...
示例2：
0 0 0 2 1
0 2 0 1 0
5个人围成一圈
'''

data = list(map(int, input().split()))

sums = sum(data)
dp = [0]*len(data)

j = 0
for i in range(1, 300):
    # 又重新来了一圈
    if j == len(data):
        j = 0

    if i % 7 == 0 or '7' in str(i):
        dp[j] += 1  # 对应人喊
    if sum(dp) == sums:
        break

    j += 1

print(" ".join(str(x) for x in dp))

