# -*- coding: utf-8 -*-
# @Time  : 2023/04/15 22:09
# @author: dtf
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
    a = [i for i in range(10000)]
    print(a)


if __name__ == '__main__':
    main()