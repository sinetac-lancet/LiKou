# -*- coding: utf-8 -*-
# @Time  : 2023/05/07 22:15
# @author: dtf

# https://dream.blog.csdn.net/article/details/130320861
# 暴力法


N = int(input())
data = []
for i in range(N):
    tmp = list(map(int, input().split()))
    data.append(tmp)
data.sort(key=lambda x: x[1])
print(data)

min_val = data[0][0]
max_val = data[-1][1]
end = max_val + 1   # 这个是核心，不然会超过列表范围
time_slice = [0]*end

for left, right in data:
    num = left
    while num < right+1:
        time_slice[num] += 1
        num += 1
print(time_slice)

res = 0
# 这样就把开头没有任务的部分删掉；2、由于是一个左闭右开的区间，因此此时用end就可以读取到最后一个元素了
for i in range(min_val, end):
    # print(time_slice[i])
    if time_slice[i] == 0:
        res += 1
    elif time_slice[i] == 1:
        res += 3
    else:
        res += 4
print(res)

