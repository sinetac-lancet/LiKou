# -*- coding: utf-8 -*-
# @Time  : 2023/03/26 10:46
# @author: dtf
# 链接：https://leetcode.cn/problems/number-of-students-unable-to-eat-lunch/solution/wu-fa-chi-wu-can-de-xue-sheng-shu-liang-fv3f5/
'''
核心：假设喜欢吃圆形三明治的学生数量为 s0，喜欢吃方形三明治的学生数量为 s1。s0 +s1 = len(students)​
解题：是一个匹配问题，三明治类型和学生口味匹配，s0或s1就-1，知道遍历所有的三明治后，剩下的就是不匹配的数量
'''
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s1 = sum(students)
        s0 = len(students) - s1
        for x in sandwiches:
            if x == 0 and s0:
                s0 -= 1
            elif x == 1 and s1:
                s1 -= 1
            else:
                break
        print('s0 = {}, s1 = {}'.format(s0, s1))
        return s0 + s1


if __name__ == '__main__':
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]
    sl = Solution()
    print(sl.countStudents(students, sandwiches))