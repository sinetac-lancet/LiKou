# -*- coding: utf-8 -*-
# @Time  : 2023/04/09 10:07
# @author: dtf

# https://dream.blog.csdn.net/article/details/129167604

'''
个人思路：
区间列表按照起点排序后，
（1）先将重叠的区间合并成一个区间
（2）计算区间相差距离，然后在连接器列表中匹配
'''

'''
贪心算法
'''

import re

# data1 = input()
# data1 = '[1,2],[3,5],[7,10],[15,20],[30,100]'
data1 = '[1,10],[15,20],[18,30],[33,40]'
list1 = re.findall('\[(.*?)\]', data1)
regions = [list(map(int, str(i).split(','))) for i in list1]
# regions.sort(key=lambda x: x[0])

# data2 = input()
data2 = '[5, 4, 3, 2]'
list2 = re.findall('\[(.*?)\]', data2)
links = list(map(int, str(list2[0]).split(',')))

print(regions)
print(links)

reg = None
i = 0
while i < len(regions):
    next = regions[i]
    if reg is None:
        reg = next
        i += 1
    elif reg[1] >= next[0]:
        if reg[1] < next[1]:
            reg[1] = next[1]
        regions.pop(i)
    else:
        reg = next
        i += 1

print(regions)
gaps = []
reg = None
for i in range(len(regions)):
    next = regions[i]
    if reg is not None:
        gap = next[0] - reg[1]
        gaps.append(gap)
    reg = next

'''
贪心算法：因为压要每一步的最优解，因此需要用for遍历
'''
gaps.sort()
links.sort()
# print(gaps)
# print(links)
count = len(gaps)   # 负责记录结果的
for i in range(len(gaps)):
    gap = gaps[i]
    for j in range(len(links)):
        if links[j] >= gap: # 负责定义限制条件
            count -= 1
            links.pop(j)
            break

print(count+1)



