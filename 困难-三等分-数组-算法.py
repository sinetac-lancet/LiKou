# -*- coding: utf-8 -*-
# @Time  : 2023/03/25 14:55
# @author: dtf
from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # 找出每一部分第一个1所在位置
        def find(x):
            s = 0
            for i, data in enumerate(arr):
                s += data
                if s == x:
                    return i

        num = len(arr)
        # 把数组arr中的1平均分成3份
        # cnt, mod = sum(arr)//3, sum(arr)%3
        cnt, mod = divmod(sum(arr), 3)
        if mod:
            return [-1, -1]
        if cnt == 0:
            # 0：首位数字；num-1：末尾数字
            return [0, num-1]

        i, j, k = find(1), find(cnt + 1), find(cnt*2 + 1)
        '''
        如果要保证分成3部分的最终结果是一样的，那么，在找到每一部分第一个1后开始同时向后遍历,
        如果在k还未到最后一个数值时，就出现了三部分的三个数不相等的情况，那么这三部分也不会是相等的
        '''
        # ！！！注意：为什么这里的条件是k<n，但是最后返回的时候是 k==n。
        # 原因：在while循环中在k移动到最后一位时，进入了循环，那么结束循环的时候k=num，即len(arr)
        while k < num and (arr[i] == arr[j] == arr[k]):
            i, j, k = i+1, j+1, k+1

        return [i-1, j] if k == num else [-1, -1]
