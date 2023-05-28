# -*- coding: utf-8 -*-
# @Time  : 2023/05/24 20:03
# @author: dtf

'''
每个车位上有一个监控器，当且仅当当前车位或者前后左右四个方向任意一个车位范围内停车时，监控器擦需要打开

输入：
    第一行 m、n表示长宽，满足1 < m, n < 20；
    后面输出m行，每行有n个0或1的整数，整数间使用一个空格隔开。0表示空位，1表示已停
输出：
    最少需要打开的监控器数量

3 3
0 0 0
0 1 0
0 0 0
5

3 3
1 0 0
0 1 0
0 0 0
6
'''

rows, cols = map(int, input().split())
grid = [[0] * (cols + 2) for _ in range(rows + 2)]
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]
for i in range(1, rows + 1):
    row = list(map(int, input().split()))
    for j in range(1, cols + 1):
        grid[i][j] = row[j - 1]
ret = 0
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        for dx, dy in dirs:
            x = i + dx
            y = j + dy
            if 1 <= x <= rows and 1 <= y <= cols and grid[x][y] == 1:
                ret += 1
                break
print(ret)

