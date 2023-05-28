# -*- coding: utf-8 -*-
# @Time  : 2023/05/25 22:26
# @author: dtf
'''
https://dream.blog.csdn.net/article/details/129075162

一个工厂有m条流水线
来并行完成n个对立的作业
该工厂设置了一个调度系统
在安排作业时，总是优先执行处理时间最短的作业
现给定流水线个数m
需要完成作业数n
每个作业的处理时间t1\t2\t3\t4

计算处理完所有作业的耗时为多少
当n > m时，首先处理时间短的m个作业流水线
其他等待
当某个作业完成时
依次从剩余作业中取处理时间最短的
进入处理

输入：

输出：
    输出处理完所有作业的总时长


3 5
8 4 3 2 10

13
说明：先安排2，3，4的三个作业
第一条流水线先完成作业
调度剩余时间最短作业为 8
第二条流水线完成作业
调度剩余时间最短的作业10
总共耗时，就是二条流水线完成作业时间13(3+10)
'''

# 流水线个数m，作业数n
def method(m, n, data):
    tasks = sorted(data)
    if n < m:
        print(max(tasks))
        return

    res = tasks[:m]
    for i in range(m, n):
        min_val = min(res)  # 每次取出最小处理时间的任务，然后安排给等待的任务
        min_idx = res.index(min_val)
        res[min_idx] += tasks[i]    # 每个流水线处理的任务时间相加
    print('res: ', res)
    print(max(res))


if __name__ == '__main__':
    m, n = map(int, input().split())
    tasks = list(map(int, input().split()))
    method(m, n, tasks)

