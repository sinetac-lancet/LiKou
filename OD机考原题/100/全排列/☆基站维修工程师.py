# -*- coding: utf-8 -*-
# @Time  : 2023/05/20 20:17
# @author: dtf


# https://dream.blog.csdn.net/article/details/129019205

'''
n个基站，已知各基站之间的距离s
基站x到基站y的距离，与基站y到基站x的距离并不一定会相同
小王从基站1出发，途径每个基站1次，然后返回基站1，需要选择一条距离最短的路

输入：
站点数n 和 各站点之间的距离
如：
    3 // 站点数
    0 2 1 //站点1到各站点的路程
    1 0 2 //站点2到各站点的路程
    2 1 0 //站点3到各站点的路程
输出：最短路程的数值
如：3
'''