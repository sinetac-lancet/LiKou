# -*- coding: utf-8 -*-
# @Time  : 2023/04/16 15:10
# @author: dtf


# https://dream.blog.csdn.net/article/details/129216367

'''
题目理解：
施肥机能效K = 果林面积 / 天数 + 1
'''


m, n = tuple(map(int, input().split()))
fields = list(map(int, input().split()))
print(m, n)
print(fields)

# res = 0
# for i in range(m):
#     val = fields[i] // n
#     if fields[i] > val*n:
#         res += (val + 1)
#     else:
#         res += val
# print(res)
