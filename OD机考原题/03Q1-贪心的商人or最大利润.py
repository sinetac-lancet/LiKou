# -*- coding: utf-8 -*-
# @Time  : 2023/04/15 22:16
# @author: dtf


# https://dream.blog.csdn.net/article/details/129216472


'''
题目理解：
每件商品需要做到以下几点：
（1）在前面某一天低价的时候买入，然后等后边某一天最高价的时候卖出，赚取差价利润
（2）如果该商品的价格是递减的，买入后不出手，或者直接不买入，默认利润为0

'''

number = int(input())
days = int(input())
items = list(map(int, input().split()))
prices = []
for i in range(days):
    tmp = list(map(int, input().split()))
    prices.append(tmp)
print(number)
print(days)
print(items)
print(prices)

# res = 0
# for i in range(days):
#     p = prices[i]
#     diff = 0 if (p[-1]-p[0]) < 0 else (p[-1]-p[0])
#     print(p)
#     print(diff)
#     res += items[i] * diff
# print(res)

'''
核心：对于题目描述中的商品可以多次买卖的理解？
答：就是只要明天的价格于今天相比有差价就买卖
'''
res = 0
for i in range(number):

    for j in range(days - 1):   # 避免超出范围，直接不让遍历到最后一天
        buy_prices = prices[i][j]
        sell_prices = prices[i][j+1]
        if buy_prices < sell_prices:
            res += (sell_prices-buy_prices)*items[i]
print(res)
