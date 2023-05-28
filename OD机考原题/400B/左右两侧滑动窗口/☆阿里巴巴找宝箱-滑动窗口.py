# -*- coding: utf-8 -*-
# @Time  : 2023/05/24 20:20
# @author: dtf

'''
藏宝地有编号从0-N的箱子，每个箱子上贴有一个数字，箱子中可能有一个黄金宝箱
黄金宝箱满足：排在它之前的所有箱子之和等于排在它之后的所有箱子数组和
第一个箱子左边部分数字和定义为0；
最后一个宝箱右边的数字和定义为0；

输出第一个满足条件的黄金宝箱编号，如果不存在黄金宝箱，请返回-1

输入描述：
    宝箱数量不小于1个，不超过1000
    宝箱上贴的数值范围不低于-1000，不超过1000
输出描述：
    第一个黄金宝箱的编号

2,5,-1,8,6
3

'''
'''
刷题理解：
    排在它之前的所有箱子之和等于排在它之后的所有箱子数组和 ==> 每次不能包含自己，只看之前的数字 和 之后的数字
                                                    ==> 或者全部都包含自己
'''


data = list(map(int, input().split(',')))
print(data)
n = len(data)
index = -1
l, r = 0, 0
for i in range(n):
    l_sums = 0
    r_sums = 0
    l = i
    while l >= 0:
        l_sums += data[l]
        l -= 1

    r = i
    while r < n:
        r_sums += data[r]
        r += 1
    print(l_sums, r_sums)
    if l_sums == r_sums:
        index = i
        break
print(index)


# def method(data):
#     n = len(data)
#     left_sum = 0
#     right_sum = sum(data)
#     for i in range(n):
#         right_sum -= data[i]
#         if left_sum == right_sum:
#             return i
#         left_sum += data[i]
#     return -1
#
#
# data = list(map(int, input().split(',')))
# res = method(data)
# print(res)


