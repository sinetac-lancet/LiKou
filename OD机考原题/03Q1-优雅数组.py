# -*- coding: utf-8 -*-
# @Time  : 2023/04/09 16:18
# @author: dtf

# https://dream.blog.csdn.net/article/details/129167706


'''
算法思路是计算一个长度为n的数组中，有多少个长度不小于k的子数组满足其中某个数字出现的次数不小于k.
具体实现：通过双重循环遍历数组中所有可能的子数组，并使用一个字典count记录当前子数组中每个数字出现的次数。
如果在子数组中发现某个数字出现的次数不小于k，则累计当前子数组的长度到res中，并推出内层循环
'''
def solve_method(N, K, arr):
    res = 0
    for i in range(N):
        count = {}
        for j in range(i, N):
            key = arr[j]
            # count.get(key, 0)表示获取原来字典内该键对应的键值； +1表示该字符又出现一次
            count[key] = count.get(key, 0) + 1
            print('count1 = ', count)
            if count[key] >= K:
                # 累加当前子数组的长度
                # 原理是：当前子数组已经有字符超过k了，因此后边的还有几个字符就还有几个子字符组
                res += N - j
                print('count2 = ', count)
                print('res = ', res)
                break
    return res


if __name__ == '__main__':
    data1 = tuple(map(int, input().split()))
    N, K = data1
    data2 = tuple(map(int, input().split()))
    print(N, K, data2)
    res = solve_method(N, K, data2)
    print(res)

