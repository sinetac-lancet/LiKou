# -*- coding: utf-8 -*-
# @Time  : 2023/05/21 12:59
# @author: dtf

# https://dream.blog.csdn.net/article/details/129031337

'''
主要目的是，给定的整数数组中找到两个非空、不相交的子集，使得它们的 异或和 相等，且它们的和最大
该算法的基本思路是使用贪心的方法 将输入的整数从小到大排序，然后通过遍历数组，尝试划分它成两个子数组，并计算每个子数组的和 及 异或和
如果两个子数组的 异或和相等， 则比较他们的和，并更新最大和

'''

'''
题目理解：
两种分配方式，求解满足A（等分）的情况下，B如果得到最大

示例1：
8
7258 6579 2602 6716 3050 3564 5396 1773

35165

'''


def method(num, data):
    data.sort(reverse=True)     # 排序。因为加快了查找
    max_num = -1
    # !!!要想平分，那么数据data必须是大于2的，因此从索引1开始遍历
    for i in range(1, num, 1):
        left_binary, right_binary = 0, 0
        left_num, right_num = 0, 0
        for j in range(0, i, 1):
            left_binary ^= data[j]
            left_num += data[j]
        for j in range(i, num, 1):
            right_binary ^= data[j]
            right_num += data[j]

        if left_binary == right_binary:
            max_num = max(max_num, max(left_num, right_num))
    return max_num


if __name__ == '__main__':
    num = int(input())
    data = list(map(int, input().split()))

    res = method(num, data)
    print(res)