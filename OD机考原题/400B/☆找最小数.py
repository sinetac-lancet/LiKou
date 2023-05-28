# -*- coding: utf-8 -*-
# @Time  : 2023/05/25 23:12
# @author: dtf
'''

https://dream.blog.csdn.net/article/details/130862079

给一个正整数NUM1，计算新正整数NUM2，NUM2为NUM1中移除N位数字后的结果，需要使得NUM2的值最小

输入：
    1、输入的第一行位一个字符串，字符串由0-9字符组成，记录正整数NUM1，NUM1长度小于32
    2、输入的第二行为需要移除的数字的个数，小于NUM1长度

输出：
    输出一个字符串，记录最小值NUM2

输入：
    2615371
    4
输出：
    131

'''

def main():
    num = input()
    n = int(input())

    stack = []
    for i in range(len(num)):
        while n > 0 and stack and stack[-1] > num[i]:
            stack.pop()
            n -= 1
        stack.append(num[i])    # 只存储最小的len(num) - n个数

    results = ''.join(stack)
    print(results)


if __name__ == '__main__':
    main()