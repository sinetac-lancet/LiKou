# -*- coding: utf-8 -*-
# @Time  : 2023/05/24 20:48
# @author: dtf

'''
同一个数轴x上有两个点的集合A和B，两个集合元素均为正整数，A,B已经按照从小到大排好序，A,B均不为空
给定一个距离R（正整数）
列出同时满足如下条件的所有（Ai,Bj）对
1、Ai <= Bj
2、Ai, Bj之间的距离小于等于R
3、在满足1，2的情况下，每个Ai只需输出距离最近的Bj
4、输出结果按Ai从小到大的顺序排序
输入：
    第一行 m, n, R
    第二行m个正整数，表示集合A
    第三行n个正整数，表示集合B

输出：
    每组数对输出一行 Ai 和 Bj，以空格隔开

4 5 5
1 5 5 10
1 3 8 8 20

1 1
5 8
5 8


'''


def method(r, a, b):
    index = 0
    res = []
    for j in a:
        tmp = [0, 0]
        while index < len(b):
            if j <= b[index] and abs(b[index] - j) <= r:
                tmp[0] = j
                tmp[1] = b[index]
                res.append(tmp)
                break
            index += 1
    return res


m, n, r = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = method(r, a, b)
for i, j in res:
    print(i, j)

