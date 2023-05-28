# -*- coding: utf-8 -*-
# @Time  : 2023/05/25 20:29
# @author: dtf

'''

输入：
    第一行

输出：
    输出n行
    表示n块磁盘容量排序后的结果

3
1G
2G
1024M
输出：
    1G
    1024M
    2G

3
2G4M
3M2G
1T
输出：
    3M2G
    2G4M
    1T

'''
import re


def method(data):
    # 根据存储容量大小排序
    data.sort(key=convert)
    for c in data:
        print(c)

def convert(data):
    size = 0
    upper = data.upper()
    # 以字母为间隔，得到所有的数字；例如：splits: ['1024', '']
    splits = re.split('[A-Z]', upper)
    print('splits:', splits)
    pos = 0
    for s in splits:
        if s == '':
            continue
        nums = int(s)
        alpha = upper[pos + len(s)]
        if alpha == 'M':
            size += nums
        elif alpha == 'G':
            size += nums * 1024
        elif alpha == 'T':
            size += nums * 1024 * 1024
        pos += len(s) + 1
    return size


if __name__ == '__main__':
    num = int(input().strip())
    data = [input().strip() for _ in range(num)]
    method(data)
