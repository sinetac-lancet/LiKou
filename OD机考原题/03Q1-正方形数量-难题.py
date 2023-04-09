# -*- coding: utf-8 -*-
# @Time  : 2023/04/08 13:31
# @author: dtf



'''
内积为零的两个向量垂直：
例如：a垂直b，则a1b1+a2b2=0

'''


def is_rect(x1, y1, x2, y2):
    distance = x1*x2 + y1*y2
    return distance


if __name__ == '__main__':
    N = int(input())
    # N个坐标点，输出可以构成的正方形的数量
    data = []
    for i in range(N):
        data.append(tuple(map(int, input().split())))
    print(N, data)

    if N < 4:
        print(0)
    else:
        res = {}
        # 双指针-滑动窗口
        i = 0
        while i < N:
            x1, y1 = data[i]
            j = i + 1
            while j < N:
                x2, y2 = data[j]
                distance = is_rect(x1, y1, x2, y2)
                if distance in res:
                    res[distance] += 1
                else:
                    res[distance] = 1
                j += 1

            i += 1
        print(res)



