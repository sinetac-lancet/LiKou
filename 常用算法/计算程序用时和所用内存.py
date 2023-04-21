# -*- coding: utf-8 -*-
# @Time  : 2023/04/15 22:05
# @author: dtf


# import timeit
# start = timeit.default_timer()
# end = timeit.default_timer()
# print(f'used time : {end - start}s')

import time
import os
import psutil


def count_time(func):
    def int_time():
        start_time = time.time()
        func()
        over_time = time.time()
        total_time = over_time - start_time
        print("程序运行了%s秒" % total_time)
    return int_time


def count_info(func):
    def float_info():
        pid = os.getpid()
        p = psutil.Process(pid)
        info_start = p.memory_full_info().uss/1024
        func()
        info_end=p.memory_full_info().uss/1024
        print("程序占用了内存"+str(info_end-info_start)+"KB")
    return float_info

@count_time
@count_info
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
    main()