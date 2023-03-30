# -*- coding: utf-8 -*-
# @Time  : 2023/03/30 21:35
# @author: dtf
import sys

while True:
    try:
        n = int(input())
        m = list(map(int, input().split()))
        x = list(map(int, input().split()))

        lst = []    # 存放砝码，例如[[2, 2, 1, 3, 3, 3]表示2个2g、1个1g、3个3g砝码
        for i in zip(m, x): # 按照对应关系，生成元组，返回可迭代对象
            lst.extend([i[0]]*i[1])

        weights = {0}   # 集合（无序，不重复集合）
        for i in lst:
            for j in list(weights): # 集合转列表
                weights.add(i + j)
                print(weights)
        print(weights)
        print(len(weights))

    except Exception as e:
        # raise e   # 调试用，但是最终提交不要使用
        break
