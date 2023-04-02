# -*- coding: utf-8 -*-
# @Time  : 2023/04/02 14:54
# @author: dtf
'''
开始-结束区间交叉任务数量
[num：（）]
初始化_max = max(num)
使用贪心算法，先按照开始时刻排序，如果交叉就更新_max
'''
import sys
# https://dream.blog.csdn.net/article/details/129250888

# num = int(input())
# task_dict = {}
# for i in range(num):
#     task_info = list(map(int, input().split()))
#     task_dict[task_info[2]] = (task_info[0], task_info[1])
#
# print(task_dict)
# # 按照键排序，默认升序
# # task_dict2 = sorted(task_dict)
# # print(task_dict2)
# # key=lambda x: x按照元组第一个元素，如果第一个相同则按照第二个，默认升序
# # task_dict2 = sorted(task_dict.values(), key=lambda x: x)    # [(2, 7), (2, 9), (4, 9)]
# # print(task_dict2)
# # # key=lambda x: x[0]按照元组第一个值排序，默认升序
# # task_dict2 = sorted(task_dict.values(), key=lambda x: x[0]) # [(2, 9), (2, 7), (4, 9)]
# # print(task_dict2)
#
# task_dict2 = sorted(task_dict.items(), key=lambda x: x)    # [(2, 7), (2, 9), (4, 9)]
# print(task_dict2)


import heapq

def deal_method(num, tasks):
    tasks.sort(key=lambda x: x[0])  # 按照开始时间升序排列，更改原始数据

    que_list = []   # 小根堆，升序
    res = 0 # 输出

    for i in range(num):
        # 如果队列中队首（最小元素）小于新任务的开始时间，那么以为该任务已经结束了，故弹出队列
        while que_list and que_list[0] <= tasks[i][0]:
            heapq.heappop(que_list) # 弹出堆最小元素

        # 将 并行度 个任务结束时间，放入队列中
        for t in range(tasks[i][2]):
            heapq.heappush(que_list, tasks[i][1])

        res = max(res, len(que_list))

    return res

num = int(input())
tasks = [list(map(int, input().split())) for i in range(num)]
res = deal_method(num, tasks)
print(res)




