# -*- coding: utf-8 -*-
# @Time  : 2023/05/25 19:25
# @author: dtf

'''
输入：
    输入压缩后的报文：
        1、不考虑无效输入，报文没有额外的空格，方括号总是符合满足要求的
        2、原始报文不包含数字，所有数字只表示重复的次数n，例如不会出现5b或3[8]的输入
输出：
    解压后的原始报文
3[k]2[mn]
kkkmnmn

3[m2[c]]
mccmccmcc

'''
import re

'''错误'''
# data = input()
# res = []
# i = 0
# while i < len(data):
#     l = data.find('[', i)
#     r = data.find(']', i)
#     if l != -1 and r != -1:
#         num = int(data[i:l])
#         chars = data[l+1:r]
#         res.append([num, chars])
#         i = r + 1
#     print(l, r)
# if res:
#     print(''.join(val*key for key, val in res))
# else:
#     print(res)


'''
3[m2[c]]
back:  <re.Match object; span=(3, 7), match='2[c]'>
groups:  2[c]
back:  <re.Match object; span=(0, 6), match='3[mcc]'>
groups:  3[mcc]
back:  None
mccmccmcc
'''
def method(data):
    pattern = re.compile(r'[0-9]+\[[a-z]+]')
    back = pattern.search(data)
    print('back: ', back)
    if back:
        groups = back.group()
        print('groups: ', groups)

        pos = groups.index('[')
        num = int(groups[:pos])
        words = groups[pos + 1:-1]

        build = ""
        build += words*num
        subs = data.replace(groups, build)
        return method(subs)
    else:
        return data


def main():
    data = input().strip()
    res = method(data)
    print(res)


if __name__ == '__main__':
    main()




