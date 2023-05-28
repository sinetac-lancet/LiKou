# -*- coding: utf-8 -*-
# @Time  : 2023/05/21 10:37
# @author: dtf

# https://blog.csdn.net/hihell/article/details/128995301
'''
1、命令字之间以 一个或多个下划线 分割

"" 双引号的作用是，当包含_这个符号的时候不会当作一个命令字，而是双引号中的会看做一个整体
比如
输入：
    2
    aaa_password_"a12_45678"_timeout__100_""_
输出：
    aaa_password_"******"_timeout_100_""
'''

'''

'''

def method(num, strs):
    commands = []
    '''
    因为要查看下划线_连续出现多少，因此使用while更合适
    '''
    data = list(strs)
    i = 0
    while i < len(strs):
        cur = data[i]
        command = ""

        if cur == '"':
            pos = strs.find('"', i+1)
            command = strs[i:pos+1]
            i = pos
        else:
            pos = strs.find('_', i)
            if pos != -1:
                command = strs[i:pos]
                i = pos + 1
            else:
                command = strs[i:]
                i = len(strs)
        if command:
            commands.append(command)
    if num < len(commands):
        commands[num] = '******'
        return '_'.join(commands)
    else:
        return 'ERROR'


if __name__ == '__main__':
    num = int(input())
    strs = input().strip()  # fdsafasfa，即还是字符串
    res = method(num, strs)
    print(res)


