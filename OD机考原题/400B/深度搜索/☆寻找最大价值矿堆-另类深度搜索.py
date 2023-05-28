# -*- coding: utf-8 -*-
# @Time  : 2023/05/27 15:37
# @author: dtf
'''
给一个由'0'（空地）、’1‘（银矿）、’2‘（金矿）组成的地图
矿堆只能由上下左右相邻的金矿或银矿连接形成，超出地图范围可以认为是空地
假设银矿价值1，金矿价值2，请找出最大价值的矿堆并输出该矿堆的价值

地图范围最大300*300
0 <= 地图元素 <= 2

输入：
    22220
    00000
    00000
    01111
输出：
    8

22220
00020
00010
01111

15

20000
00020
00000
00111

3

'''

# 错误
# def method(data):
#     row, col = len(data), len(data[0])
#     dp = [[0]*col for _ in range(row)]
#     for i in range(row):
#         tmp = data[i]
#         for j in range(col):
#             dp[i][j] = int(tmp[j])
#     print(dp)
#     res = 0
#     for i in range(row):
#         for j in range(col):
#             total = 0
#             directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#             for dirs in directions:
#                 nx = i + dirs[0]
#                 ny = j + dirs[1]
#                 if 0 <= nx < row and 0 <= ny < col and dp[nx][ny] > 0:
#                     if dp[nx][ny] == 2:
#                         total += dp[nx][ny] * 2
#                     else:
#                         total += dp[nx][ny]
#             if total:
#                 res += total
#             else:
#                 res = max(res, total)
#             print(res, total)
#     print(res)
#
#
# data = []
# while True:
#     try:
#         data.append(input().strip())
#     except EOFError:
#         break
# print(data)
# method(data)



def main():
    map = [[0] * 300 for _ in range(300)]
    result = 0
    i = 0
    while True:
        try:
            s = input()
            for j in range(len(s)):
                map[i][j] = int(s[j])
            i += 1
        except EOFError:
            break

    visited = [[False] * 300 for _ in range(300)]
    for i in range(300):
        for j in range(300):
            if map[i][j] > 0 and not visited[i][j]:
                value = dfs(i, j, map, visited)
                result = max(result, value)

    print(result)


def dfs(x, y, map, visited):
    if x < 0 or x >= 300 or y < 0 or y >= 300 or map[x][y] == 0 or visited[x][y]:
        return 0

    visited[x][y] = True
    value = map[x][y]
    result = (
        dfs(x + 1, y, map, visited)
        + dfs(x - 1, y, map, visited)
        + dfs(x, y - 1, map, visited)
        + dfs(x, y + 1, map, visited)
        + value
    )
    return result


if __name__ == "__main__":
    main()



