# -*- coding: utf-8 -*-
# @Time  : 2023/05/21 19:37
# @author: dtf
# https://blog.csdn.net/hihell/article/details/129019167

'''
输入：
    排序前的小朋友，例如4 3 5 7 8
输出：
    排序后的小朋友，例如：4（高） 3（矮） 7（高） 5（矮） 8（高）
    输出结果为最小移动距离，只有5和7交换了距离，移动距离为1
'''
# 注意输入可能存在非法字符xxx
data = []
try:
    data = list(map(int, input().split()))
except:
    print(data)
    exit()
'''
需要构建：高矮高矮...
因此，偶数位为高、奇数位为矮
'''
dp = [0] * len(data)
for i in range(len(data) - 1):
    # 偶数位，应为高
    if i%2 == 0 and data[i] < data[i+1]:
        data[i], data[i+1] = data[i+1], data[i]
    # 奇数位，应为矮
    if i%2 == 1 and data[i] > data[i+1]:
        data[i], data[i+1] = data[i+1], data[i]
res = " ".join(str(data[i]) for i in range(len(data)))
print(res)


