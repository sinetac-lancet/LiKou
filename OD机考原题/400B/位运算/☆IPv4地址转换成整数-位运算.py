# -*- coding: utf-8 -*-
# @Time  : 2023/05/21 15:45
# @author: dtf
# https://dream.blog.csdn.net/article/details/129088277

'''
每一节范围分别为(1-128)#(0-255)#(0-255)#(0-255)
转化为一个32位整数，即乘以 8

输入：
    输入一行，虚拟IPv4地址格式字符串
输出：
    输出以上，按照要求输出整型或者特定字符
示例1：
输入：1#2#3
输出：invalid OP
说明：将IP地址转换成32位整数的算法。IP地址是由四个数字（每个数值在0-255之间）组成，
同点号分隔。例如，192.168.0.1可以转换成3232235521的32位整数。算法首先检查字符串是否符合IP地址的格式，如果格式正确，则计算32位整数。

示例2：
输入：100#101#1#5
输出：1684340997
'''

ip = input()

strs = ip.split('#')
n = len(strs)
count = 0
is_valid = True
if n == 4:
    # 每一节范围分别为(1 - 128)  # (0-255)#(0-255)#(0-255)
    for i in range(n):
        val = int(strs[i])
        if i == 0 and (val < 1 or val > 128):
            is_valid = False
            break
        elif val < 0 or val > 255:
            is_valid = False
            break
        '''
        位运算：
        1、<<
            a = 2
            print(a << 3)  # 相当于a 乘 2的3次方
        2、>>
            a = 32
            print(a >> 3)  # 相当于a 除 2的3次方
        '''
        count += val << (8*(3-i))
        print('count: ', count)

else:
    is_valid = False

if is_valid:
    print(count)
else:
    print('invalid OP')
