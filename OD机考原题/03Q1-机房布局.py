# -*- coding: utf-8 -*-
# @Time  : 2023/04/08 15:56
# @author: dtf


# https://dream.blog.csdn.net/article/details/129167580

'''
字符匹配，
连续区间-->滑动窗口
'''

# data = input()
# print(data)
# if len(data) < 3:
#     print(-1)
#     exit()
# elif len(data) == 3:
#     num = [1 if 'I' == j else 0 for j in data]
#     if sum(num) >= 2:
#         print(-1)
#         exit()
#
# N = len(data)
# left = 0
# right = 0
# res = []
# num = 0
# while right < N and right < N:
#     res.append(data[right])
#     right += 1
#     if data[right] != res[0]:
#         num = right - left
#         while


from collections import deque


'''
理解：机柜与机柜中间要有间隔，不然无法放置电箱，故
I       1
M       -1
MM      -1
MIM     1
MIIM    2
'''
def solve_method(line):
    n = len(line)
    stack = deque() # 双端队列
    stick = False

    for i in range(n):
        if line[i] == "M":  # 当前是否为机柜
            # 判断left 和 right 是否越界，与 是否有和它紧邻的机柜，返回-1（无解）
            left = i - 1 < 0 or line[i - 1] == "M"
            right = i + 1 >= n or line[i + 1] == "M"
            if left and right:
                return -1

            '''
            以下代码的理解：
            （1）存储每一个M的区间间隔
            （2）将MIM这种类型合并成一个，因为这种情况只需要一个机箱
            '''
            # 使用一个栈来存储，当前机柜所处的区间，即[i-1, i+1]，注意不要越界
            range_ = [max(0, i - 1), min(n - 1, i + 1)]
            # 判断新区间与前一个区间是否紧邻，如果相邻，则将其合并到一个连续区间，如MIM
            # 如果不紧邻那么就不用任何处理，直接运行到stack.append(range_)正常跟新区间即可
            if stack and not stick:
                e1 = stack[-1][1]
                s2 = range_[0]

                if e1 == s2:
                    stack.pop()
                    stick = True
            else:
                stick = False
            stack.append(range_)

    return len(stack)


if __name__ == "__main__":
    line = input()
    print(solve_method(line))


