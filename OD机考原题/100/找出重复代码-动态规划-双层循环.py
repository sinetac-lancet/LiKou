# -*- coding: utf-8 -*-
# @Time  : 2023/05/20 20:17
# @author: dtf


# https://dream.blog.csdn.net/article/details/129019205

'''
题目：找出两行代码中的 最长公共子串
输入描述：
    输出参数text1, text2分别代表两行代码
输出描述：
    输出任意最长公共子串
示例1：
输入：
    hello123world
    hello123abc4
输出：
    hello123
'''

'''
编码思路：
动态规划：用 dp[i][j]表示str1中的前i个字符 和 str2的前j个字符的 最长公共子序列的长度

'''

# 动态规划
import sys


def main():
    str1 = input().strip()
    str2 = input().strip()
    # 多创建一个，后续dp[i][j] = dp[i - 1][j - 1] + 1可以适配i-1=0的情况
    dp = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    # print(dp)
    # print(len(dp))
    # exit()
    max_len = 0
    end = 0
    # 暴力法，双层循环遍历匹配
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:          # 如果元素相同
                # 这个就是一个累加的过程，如果前面是相同的，那么dp[i - 1][j - 1]=1，反之为0，无伤大雅
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end = i - 1     # 这个随着i的增大，最后落到最靠后的适当位置
    print(str1[end - max_len + 1:end + 1])


if __name__ == '__main__':
    sys.exit(main())
