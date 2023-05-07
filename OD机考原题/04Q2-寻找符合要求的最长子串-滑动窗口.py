# -*- coding: utf-8 -*-
# @Time  : 2023/05/07 20:45
# @author: dtf


'''
子串条件：
1、该子串中的任意一个字符最多出现次数为2
2、该子串不包含指定的某个字符
'''

target_char = input()
total_str = input()

N = len(total_str)
left, right = 0, 0
nums = 0
res = {}

while right < N:
    temp = total_str[right]
    if temp == target_char:
        res.clear()
        left = right + 1
        continue
    res[temp] = res.get(temp, 0) + 1    # 如果res中不存在key=temp，那么把键值初始化为0
    if res[temp] == 3:
        rm_temp = total_str[left]
        res[rm_temp] -= 1
        left += 1
    # print(res)
    nums = max(nums, right - left + 1)
    right += 1
print(nums)