# -*- coding: utf-8 -*-
# @Time  : 2023/03/25 22:39
# @author: dtf
class Solution:
    def minOperations(self, s: str) -> int:
        # 如果第一个字符为0。则，交替字符串需要将偶数维上的0 和 奇数位置上的1 做翻转
        a = s[0::2].count('1') + s[1::2].count('0')
        print('a = ', a)
        print(s[0::2].count('1'), s[1::2].count('0'))
        # 如果第一个字符为1。则，交替字符串需要将偶数维上的1 和 奇数位置上的0 做翻转
        b = s[0::2].count('0') + s[1::2].count('1')
        print('b = ', b)
        print(s[0::2].count('0'), s[1::2].count('1'))

        return min(a, b)


if __name__ == '__main__':
    s = "0100"
    sl = Solution()
    print(sl.minOperations(s))
