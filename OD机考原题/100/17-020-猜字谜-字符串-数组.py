# -*- coding: utf-8 -*-
# @Time  : 2023/05/15 20:09
# @author: dtf

# https://dream.blog.csdn.net/article/details/129103143

'''
满足以下任一条件都属于猜中：
1、变换顺序以后一样的，比如 nwes 跟 news
2、字母去重以后一样的，比如 woood 跟 wod

输入：
    1、谜面单词列表，以,分隔
    2、谜底库单词列表，以,分隔
输出：
    匹配到正确单词列表，以,分隔
    如果找不到，返回Not found
示例1：
输入：
conection
connection,todday
输出：
connection

示例2：
输入：
bdni,wooood
bind,wrong,wood
输出：
bind,wood
'''

'''
编码思路：
    将需要检查的字符串和目标字符串去重排序，比较是否相等，全部都不相等则输出Not found
'''

import sys

# 去重排序
def convert(strs):
    for i in range(len(strs)):
        tmp = set()
        s = strs[i]
        for c in s.lower():
            tmp.add(c)
        res = ''.join(sorted(tmp))
        strs[i] = res
    return strs


def method(inputs, data):
    copy_str = inputs.copy()
    seq1 = convert(inputs)
    seq2 = convert(data)

    res = []
    for s1 in seq1:
        # 匹配谜底库中所有的词条
        for i in range(len(seq2)):
            if s1 == seq2[i] and inputs[i] not in res:
                res.append(copy_str[i])
    if len(res) == 0:
        print('not found')
    else:
        print(','.join(res))


inputs = list(map(str, input().split(',')))
data = list(map(str, input().split(',')))
print(inputs)
print(data)
method(inputs, data)






