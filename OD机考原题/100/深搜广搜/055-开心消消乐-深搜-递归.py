# -*- coding: utf-8 -*-
# @Time  : 2023/05/15 19:42
# @author: dtf


# https://dream.blog.csdn.net/article/details/129045100

'''
现需要将矩阵中所有1进行反转为0，规则如下：
输入：
    第一行 输入两个整数，分别表示矩阵的行数N和列数M
    接下来N行表示矩阵的初始值，每行均为M个数
输出：
    一个整数，表示最少需要点击的次数

示例1：
3 3
1 0 1
0 1 0
1 0 1
输出：1
上述样例中，四个角1军在中间1的相邻8个方向上，因此只需要点击一次
'''

'''
编码思路：
    深度优先遍历，每当遍历一个1，就将它加入队列，并将队列的所有元素周围的1设为0，然后递归调用。
    
题目理解：
    当点击一个位置的1，于其相邻8个方向的如果为1也会翻转为0
    与此同时，当这8个方向上的某些位置1一但发生自动翻转，又会触发8个方向上1的自动翻转
    是一个递归的状态
'''

def method(row, col, data):
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    directions = []
    for i in dx:
        for j in dy:
            if i == 0 and j == 0:
                pass
            else:
                directions.append((i, j))
    print('directions: ', directions)

    times = 0
    # 遍历所有位置，得到所有1的坐标
    for i in range(row):
        for j in range(col):
            val = data[i][j]
            if val == 1:
                times += 1
                axis = []
                axis.append([i, j])
                print('axis: ', axis)
                change(row, col, axis, data, directions)

    return times

def change(row, col, axis, data, directions):
    # print('axis2: ', axis)
    if not axis: return
    cur = axis.pop(0)
    # print('cur: ', cur)

    # 8个方向
    for d in directions:
        nx = cur[0] + d[0]
        ny = cur[1] + d[1]
        if 0 <= nx < row and 0 <= ny < col and data[nx][ny] == 1:
            data[nx][ny] = 0        # 将1转为0
            axis.append([nx, ny])   # 记录原来为1的坐标
    change(row, col, axis, data, directions)    # 递归调用，遍历axis中所有坐标


if __name__ == '__main__':
    row, col = map(int, input().split())
    data = []
    for i in range(row):
        data.append(list(map(int, input().split())))
    res = method(row, col, data)
    print(res)
