# -*- coding: utf-8 -*-
# @Time  : 2023/05/05 23:14
# @author: dtf


# https://dream.blog.csdn.net/article/details/129217054


# https://dream.blog.csdn.net/article/details/129083500



import sys


def solve_method(line):
    split = line.split(" ")
    ints = [0] * (len(split) + 1)
    minValue = sys.maxsize
    minPos = 0

    for i in range(1, len(ints)):
        ints[i] = int(split[i - 1])
        if i > 1 and ints[i] != -1 and ints[i] < minValue:
            minValue = ints[i]
            minPos = i
    way = []
    while minPos >= 1:
        way.append(ints[minPos])
        minPos //= 2
    way.reverse()

    for i in range(len(way)):
        print(way[i], end='')
        if i != len(way) - 1:
            print(" ", end='')


if __name__ == '__main__':
    solve_method(input())
