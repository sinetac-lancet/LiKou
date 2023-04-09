# -*- coding: utf-8 -*-
# @Time  : 2023/04/09 15:45
# @author: dtf

# https://dream.blog.csdn.net/article/details/129167638

'''
个人思路：找出一个组合，使其和最大接近最大存储大小

（1）排序
（2）求差值，得到列表


'''

max_file = int(input())
files = list(map(int, input().split()))
files.sort()
print(max_file)
print(files)

res = []
num = 0
for i in range(len(files)):
    j = i + 1
    while j < len(files):
        if sum(res) > max_file:
            num = max(num, sum(res)-files[j])
            res = []
        res.append(files[j])
        j += 1
print(num)


