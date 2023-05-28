# -*- coding: utf-8 -*-
# @Time  : 2023/05/24 21:25
# @author: dtf
# https://dream.blog.csdn.net/article/details/129095353

'''
题目：
    小组中每位都有一张卡片，卡片时6位以内的正整数，将卡片连起来可以组成多种数字。计算组成的最大数字
输入：
    小组中最多25个人
输出：
    最大数字字符串

22,221
22221

4589,101,41425,9999
9999458941425101
'''
'''
典型的全排列问题：给出一个字符串，要求重新排列，得到最大数
采用深度优先搜索算法求解，找到所有排列的可能性，并将其按照字符串大小排序，输出最大数

要注意状态的保存和回溯，以及在搜索时如何遍历状态空间。
在这道题中，我们通过记录已经使用的数字来遍历状态空间。

'''

def method(data):
    dp = []

    def dfs(s, subs):
        if len(s) == len(data):
            dp.append("".join(s))
        else:
            for i, c in enumerate(data):
                if not subs[i]:
                    subs[i] = True
                    dfs(s + [c], subs)
                    subs[i] = False

    dfs([], [False]*len(data))
    dp = sorted(dp, reverse=True)
    print(dp)
    print(dp[0])


data = input().split(',')
method(data)


