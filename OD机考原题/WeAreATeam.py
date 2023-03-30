# -*- coding: utf-8 -*-
# @Time  : 2023/03/29 22:39
# @author: dtf


if __name__ == '__main__':
    n = int(input())
    m = []
    for i in range(n):
        m.append(tuple(map(int, input().split())))
    print(n, m)
    if n < 1 or len(m) > 100000:
        print('Null')
    dp = []
    for i in range(len(m)):
        a, b, c = m[i]
        if (c != 0 and c != 1) or (a < 1 or a > n) or (b < 1 or b > n):
            print('da pian zi')
        if c == 0:
            pass
        elif c == 1:
            dp.append(m[i])
