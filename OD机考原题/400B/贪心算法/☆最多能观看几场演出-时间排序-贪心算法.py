# -*- coding: utf-8 -*-
# @Time  : 2023/05/27 15:06
# @author: dtf

'''
https://dream.blog.csdn.net/article/details/130876955

连续观看的演出最少有15分钟的时间间隔，想尽可能多的观看演出，给出演出时间表

输入：
    第一行 一个数，表示演出场数
    接下来N行，每行两个空格分割的整数，第一个整数T表示演出的开始时间，第二个整数L表示演出的持续时间，
    T和L的单位为分钟，0<=T<=1440，0<=L<=100
输出：
    最多能观看的演出场数

2
720 120
840 120

1

'''

# num = int(input())
# data = []
# for _ in range(num):
#     start, times = map(int, input().split())
#     data.append([start, start+times])
# data.sort(key=lambda x: x[0])
# for i in range(len(data)-1):
#     if data[i+1][0] <= data[i][1]:
#         if data[i+1][1] >= data[i][1]:
#             data[i][1] = data[i+1][1]
#         data.pop(i+1)
# print(data)


'''
时间段的排序和贪心策略
如果当前时间段起始时间 与 前一个时间段的结束时间之间 大于等于15分钟，则表示多增加一场
'''
num = int(input())
data = []
for _ in range(num):
    start, times = map(int, input().split())
    data.append([start, start+times])
data.sort(key=lambda x: x[1])

t = data[0][1]
res = 1
for i in range(1, len(data)):
    l, r = data[i][0], data[i][1]
    if l - t >= 15:
        res += 1
        t = r
print(res)



