# -*- coding: utf-8 -*-
# @Time  : 2023/05/07 15:40
# @author: dtf


'''
输入示例：
1                   # 表示仅有一行输入
7 3 4 5 6 5 12 13   # 表示有7个长度的边

'''


def count_triplets(lines, start_index):
    nums = 0
    for i in range(start_index, len(lines)-2):
        a = lines[i]
        if a == 0: continue
        for j in range(i+1, len(lines)-1):
            b = lines[j]
            if b == 0: continue
            for k in range(j+1, len(lines)):
                c = lines[k]
                if c == 0: continue
                if (a * a + b * b) == c * c:
                    lines[i], lines[j], lines[k] = 0, 0, 0
                    nums = max(nums, count_triplets(lines, i + 1) + 1)  # 递归
                    lines[i], lines[j], lines[k] = a, b, c
    return nums


row = int(input())
data = list(map(int, input().split()))
print(row)
print(data)
nums = count_triplets(data, 0)
print(nums)
