# -*- coding: utf-8 -*-
# @Time  : 2023/04/05 10:36
# @author: dtf


'''
题目理解：
忽略大小写、先后顺序。
只需要密码字母 和 箱子密码串中所有字母对的上。例如 abc  A2c4b可以匹配

2、注意：
（1）523[]这样的无字母类型
'''


key_str = list(input().upper())
box_str = input().split(" ")
print(key_str, box_str)

res, number = [], -1
for i in range(len(box_str)):
    new_str = ""
    for j in box_str[i]:
        if j.isalpha(): # 判断是否为字母（不区分大小）
            new_str += j
    res.append(new_str.upper())
for idx, data in enumerate(res):
    if len(data) == len(key_str) and all(char in key_str for char in data):
        number = idx + 1
        break
print(number)

