# -*- coding: utf-8 -*-
# @Time  : 2023/04/02 9:50
# @author: dtf

import sys


# data = sys.stdin.readline()
data = input()
ch = input()

# print(data, ch)
hash_list = {}
for c in data:
    c = c.upper()
    if c == ' ':
        continue
    if c in hash_list:
        hash_list[c] += 1
    else:
        hash_list[c] = 1

# print(hash_list)
ch = ch.upper()
print(hash_list[ch] if ch in hash_list else 0)