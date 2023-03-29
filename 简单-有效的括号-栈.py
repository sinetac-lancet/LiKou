# -*- coding: utf-8 -*-
# @Time  : 2023/03/26 15:01
# @author: dtf

# https://leetcode.cn/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode-solution/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


# 链接：https://leetcode.cn/problems/valid-parentheses/solution/valid-parentheses-fu-zhu-zhan-fa-by-jin407891080/
class Solution2:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False
        return len(stack) == 1





