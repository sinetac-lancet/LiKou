# -*- coding: utf-8 -*-
# @Time  : 2023/05/21 9:45
# @author: dtf


# https://blog.csdn.net/hihell/article/details/129004964

def method(num):
    binary = bin(num)[2:]
    print(binary)
    n = len(binary)
    res = ""
    for i in range(n, 0, -7):   # 倒序
        print(i)
        st = max(i-7, 0)
        cur = binary[st:i]
        if len(cur) < 7:
            head = '0' * (7 - len(cur))
            cur = head + cur
        # 将当前的第一位置 置为0或者1，代表最高位的符号位
        cur = '0' + cur if i - 7 <= 0 else '1' + cur
        # 利用内置函数int()将二进制转为10进制，hex()将10进制转为16进制
        # upper()将其转为大写字母，最后利用zfill()函数是的十六进制的位数始终为2位
        hex_val = hex(int(cur, base=2)).upper()[2:].zfill(2)
        res += hex_val
    print(res)


if __name__ == '__main__':
    num = int(input().strip())
    method(num)