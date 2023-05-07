# -*- coding: utf-8 -*-
# @Time  : 2023/05/07 20:09
# @author: dtf


local = int(input())
data = []
for i in range(local):
    tmp = list(map(int, input().split()))
    data.append(tmp)
print(data)
# 先按照left排序，如果left相同的按照right排序
data.sort(key=lambda x: (x[0], x[1]))
print(data)

# 在指定的距离上找到最佳的服务中心点，需要每次加1遍历
min_val = data[0][0]
max_val = data[-1][1]
res = float('inf')
for i in range(min_val, max_val):   # 完成所有位置遍历
    cur_res = 0
    for left, right in data:
        if right < i:
            cur_res += i - right
        elif left > i:
            cur_res += left - i

    res = min(res, cur_res)         # 每个位置都会得到一个距离和，找出最小的距离和

print(res)
