# -*- coding: utf-8 -*-
# @Time  : 2023/05/21 21:47
# @author: dtf
# https://dream.blog.csdn.net/article/details/129045077

'''

相对于探险队总部的最远的足迹位置。
1、仪器记录坐标时，坐标的数据格式（x, y），如（1， 2），（100，200）
其中0 < x < 1000, 0 < y < 1000，同时存在非法坐标如（01，1），（1，01），（0，100）属于非法坐标
2、设定探险队总部的坐标为（0，0）某位置相对总部的距离为x*x+y*y
3、若两个坐标的相对总部的距离相同则第一次到达的坐标为最远足迹
4、若记录中的坐标都不合法输出总部坐标（0，0）
备注：不需要考虑双层括号嵌套的情况比如sfsdfsd((1,2))

输入：
    字符串表示记录仪中的数据如：
    ferg(3,10)a13fdsf3(3,4)f2r3rfasf(5,10)
输出：
    字符串表示最远足迹到达如：（5，10）
说明：记录仪中的合法坐标有三个（3，10）（3，4）（5，10）
'''

# ！！！代码经典 ！！！
inputs = input()

index = 0
x, y = 0, 0
max_distance = 0
l, r = 0, 0

while True:
    # 每次截取一部分
    inputs = inputs[index:]
    l = inputs.find('(')
    r = inputs.find(')')
    # 没有()那么l = -1
    if l == -1:
        break

    sub_str = inputs[l+1:r]
    split = sub_str.split(',')

    # !!!匹配开头字符
    if not split[0].startswith('0') and not split[1].startswith('0'):
        a = int(split[0])
        b = int(split[1])

        tmp = a * a + b * b
        if max_distance < tmp:
            x = a
            y = b
            max_distance = tmp
    index = r + 1
print('({},{})'.format(x, y))