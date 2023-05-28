# -*- coding: utf-8 -*-
# @Time  : 2023/05/25 23:06
# @author: dtf


'''

统计公司访问最多的网页URL topN
设计一个算法，可以高效动态统计TopN的页面

输入：
    每一行 是一个URL或一个数字
    如果URL代表一段时间内的网页访问
    如果是一个数字N代表本次需要输出TopN个URL
输出：
    每行输入对应一行输出
    输出按访问次数排序的前N个URL，用逗号分割
    输出要求：
        1、每次输出要统计之前的所有输入，不仅是本次输入
        2、如果有访问次数相等的URL，按URL的字符串字典序升序排列，输出排序靠前的URL
输入：
    news.qq.com
    news.sina.com.cn
    news.qq.com
    news.qq.com
    game.163.com
    game.163.com
    www.huawei.com
    www.cctv.com
    3
    www.huawei.com
    www.cctv.com
    www.huawei.com
    www.cctv.com
    www.huawei.com
    www.cctv.com
    www.huawei.com
    www.cctv.com
    www.huawei.com
    3
输出：
    news.qq.com,game.163.com,news.sina.com.cn
    www.huawei.com,www.cctv.com,news.qq.com


'''

from collections import defaultdict
import sys

top_map = defaultdict(int)


def solve_method(line):
    if not line.isdigit():   # 不是数字
        top_map[line] += 1
    else:               # 输入数字
        n = int(line)
        sorted_list = sorted(top_map.items(), key=lambda x: x[1], reverse=True)
        for i in range(n):
            print(sorted_list[i][0], end="")
            if i != n - 1:
                print(",", end="")
        print()


for line in sys.stdin:
    solve_method(line.strip())

