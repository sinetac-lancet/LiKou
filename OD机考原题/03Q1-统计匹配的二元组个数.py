# -*- coding: utf-8 -*-
# @Time  : 2023/04/15 21:44
# @author: dtf


# https://dream.blog.csdn.net/article/details/129216445
import time
from 常用算法.tools import *


def main():
    M, N = 5, 4
    lst_a = [1, 2, 3, 4, 5]
    lst_b = [4, 3, 2, 1]
    # M = int(input())
    # N = int(input())
    # lst_a = list(map(int, input().split()))
    # lst_b = list(map(int, input().split()))
    print(M, N)
    print(lst_a, lst_b)

    res = []
    for i, val1 in enumerate(lst_a):
        for j, val2 in enumerate(lst_b):
            if val1 == val2:
                res.append((i, j))
    print(res)
    print(len(res))


if __name__ == '__main__':
    start_time = time.time()
    main()
    over_time = time.time()
    total_time = over_time - start_time
    print("程序运行了%s秒" % total_time)


