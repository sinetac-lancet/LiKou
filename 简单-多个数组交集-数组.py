# -*- coding: utf-8 -*-
# @Time  : 2023/03/26 11:28
# @author: dtf
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        '''
        找出输入数组中，长度最短的元素数组，然后遍历该数组，如果其他数组都包含则保留，反之删除，最后升序排列输出
        '''
        nums.sort()
        print(nums)
        res = []
        for i in nums[0]:
            key = 0
            for j in nums:
                if i not in j:
                    key -= 1
            if key == 0:
                res.append(i)
        print(res)
        print(len(res))

        return sorted(res) if len(res) > 0 else []


if __name__ == '__main__':
    students = [[3,1,2,4,5],[2,1,3,4],[3,4,5,6]]
    sl = Solution()
    print(sl.intersection(students))