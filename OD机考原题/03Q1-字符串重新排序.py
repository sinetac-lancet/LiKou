# -*- coding: utf-8 -*-
# @Time  : 2023/04/11 20:37
# @author: dtf


# https://dream.blog.csdn.net/article/details/129216114


from collections import defaultdict


def main():
    data = input().split(' ')
    print(data)

    word_freq = defaultdict(int)    # 单词重复次数
    for s in data:
        word_sort = "".join(sorted(s))  # 字符串按照字母顺序排序
        word_freq[word_sort] += 1

    print('word_freq = ', word_freq)
    # 将键值对以元组的形式存放
    sort_freq = sorted(word_freq.items(), key=lambda x: (-x[1], len(x[0]), x[0]))
    print('sort_freq = ', sort_freq)

    res = " ".join(val*num for (val, num) in sort_freq)
    print(res[:-1])

# 测试
sort_freq =  [('in', 2), ('eht', 2), ('My', 1), ('is', 1), ('not', 1), ('arsy', 1), ('ehosu', 1), ('eiirsst', 1)]
res = []
for (val, num) in sort_freq:
    for _ in range(num):
        res.append(val)
print(res)
bb = " ".join(val for val in res)
print(bb)

if __name__ == '__main__':
    # main()
    pass