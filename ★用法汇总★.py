# -*- coding: utf-8 -*-
# @Time  : 2023/04/09 19:52
# @author: dtf



# 我们在统计一句话中每个单词出现的次数，会使用字典数据结构，并使用如下代码进行更新记数：
count = {}

for word in A.split():
    count[word] = count.get(word, 0) + 1