# -*- coding: utf-8 -*-
# @Time  : 2023/05/27 10:34
# @author: dtf

'''
https://dream.blog.csdn.net/article/details/130876835

直线上种树，给定坑位的数量和位置，以及需要种多少棵树苗，问树苗之间的最小间距是多少，可以保证种的最均匀（两棵树苗之间的最小间距最大）
即，尽可能均匀拉开距离
输入：
    第一行 坑位数量
    第二行 坑位位置
    第三行 需要种植的树苗数量
输出：
    树苗之间的最小间距

7
1 3 6 7 8 11 13
3

6
说明：三棵树苗分别种在1， 7， 13的位置，可以保证种的均匀，树苗之间的最小间距为6
'''


def method(data, num):
    data.sort()
    # 初始值，整个坑位位置间隔大小
    left, right = 0, data[-1] - data[0]
    ans = -1            # 记录最小间距
    while left <= right:
        mid = left + (right-left)//2    # 预估 剩余间隔内，下一棵树苗栽种的中间位置
        count = 1       # 记录树苗数量
        pre = data[0]                   # 记录前一棵树苗
        print('mid: ', mid)
        print('pre: ', pre)
        for i in range(1, len(data)):
            if data[i] - pre >= mid:    # 满足可以使最小间隔 最大
                count += 1
                pre = data[i]           # 记录前一棵树苗

                if count >= num:
                    ans = mid
                    left = mid + 1
                    break
            # print('mid2: ', mid)
            # print('pre2: ', pre)
        if count < num:
            right = mid - 1
    return ans


def main():
    num1 = int(input())
    data = list(map(int, input().split()))
    num2 = int(input())
    res = method(data, num2)
    print(res)


if __name__ == '__main__':
    main()



