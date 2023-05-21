# -*- coding: utf-8 -*-
# @Time  : 2023/05/20 17:20
# @author: dtf

# https://dream.blog.csdn.net/article/details/130419500
'''
n * m二维矩阵useTime，其中
useTime[i][i]=10 表示服务i自动启动加载需要消耗10s，
useTime[i][j]=1 表示服务i启动依赖服务j启动完成
useTime[i][k]=0 表示服务i启动不依赖服务k

输出描述：最少需要等待多少时间，可以堆最后一个服务进行集成测试

输入：
3
5 0 0
1 5 0
0 1 5
输出：15

说明：服务1、2、3自启动需要5s\1s\0s
'''


def method(n, data):
    target = n - 1  # 目标服务，即最后一个服务

    # 每个服务的前置依赖服务
    up_stream = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            #
            if i != j and data[i][j] == 1:
                up_stream[i].append(j)

    # 保存服务列表
    service_list = []
    service_list.append(up_stream[target])

    while service_list:
        up_stream



n = int(input())
data = [list(map(int, input().split()))]
res = method(n, data)
print(res)


