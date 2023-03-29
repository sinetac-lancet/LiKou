# -*- coding: utf-8 -*-
# @Time  : 2023/03/29 20:26
# @author: dtf


'''
士兵过河：动态规划问题，主要求解在一定时间内，完成一些任务所需要付出的最小代价；
其中，任务代价由两部分组成：一个是任务本身的代价，另一个是等待其他任务的代价
'''

# def main(N, T, A):
#     num_people, low_time = 0, 0
#     if sum(A) <= T:
#         return str(N), str(sum(A))
#     i = 0
#     while num_people <= N and low_time <= T:
#         if max(A[i], A[i+1]) <= T:
#             low_time += max(A[i], A[i + 1])
#             num_people += 2
#             i += 1
#             min_time = min(A[i], A[i+1])
#             low_time += min_time


def short_time(i, j):
    return i if i*10 < j else j


if __name__ == '__main__':
    n = int(input())
    t = int(input())
    a = sorted(map(int, input().split()))   # 返回升序排列的新数组对象
    print(n, t, a)
    dp = [0]*n
    # 动态规划
    if a[0] > t:
        print('0 0')
    else:
        dp[0] = a[0]
        if n > 1:
            dp[1] = short_time(a[0], a[1])
            if dp[1] > t:
                print("1 " + str(dp[0]))
            else:
                '''
                数组a是按照升序排列的，故a[0]的时间最短。
                
                '''
                for i in range(2, n):
                    '''
                    具体思路：计算完成这个任务所需要的最小代价，然后根据这个代价更新后续任务的最小代价。
                    在计算代价过程中，需要考虑 当前任务和前面任务之间的时间差，以及前面任务的最小代价
                    '''
                    '''
                    # a[0] + short_time(a[0], a[i])
                    （需要a[0]去往返拉人，则需要加上等待a[0]的时间） + （short_time(a[0], a[i]) 表示比较下是让a[0]独自划船，还是两人一起划）
                    # ==>
                    '''
                    dp[i] = min(dp[i-1] + a[0] + short_time(a[0], a[i]),
                                dp[i-2] + a[0] + short_time(a[i-1], a[1]) + a[1] + short_time(a[0], a[1]))
                    if dp[i] > t:
                        # 因为i是从2开始，代表a中的第三个数字
                        # 但是dp索引就得是i-1，因为dp索引是从0开始
                        print(str(i) + " " + str(dp[i-1]))
                        break

        else:
            print(str(n) + " " + str(dp[n-1]))