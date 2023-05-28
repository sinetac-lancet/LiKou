# -*- coding: utf-8 -*-
# @Time  : 2023/05/25 20:27
# @author: dtf

'''
https://blog.csdn.net/hihell/article/details/129103167?ops_request_misc=&request_id=&biz_id=&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~koosearch~default-1-129103167-null-null.268^v1^koosearch&utm_term=%E5%8F%A0%E6%94%BE%E4%B9%A6%E7%B1%8D&spm=1018.2226.3001.4450


书籍的长宽对应（l, w），如果书A的长宽都比B长宽大时，则允许将B排列放在A上面，
有一组书籍，叠放要求，书籍不能旋转，请计算最多能有多少个规格书籍能叠放在一起

输入：
    输入： books = [[20, 16], [15, 11], [10, 10], [9, 10]]
输出：
    输出：3
    说明：最多三个规格的书籍叠放在一起，从下到上依次是[20, 16], [15, 11], [10, 10]

'''

import sys


class Book:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    # 重载 < 比较运算符，即 self < other
    # 返回真，则 self other; 返回假，则other self
    def __lt__(self, other):
        # 书A的长宽都比B长宽大时，则允许将B排列放在A上面
        if self.l >= other.l and self.w >= other.w:
            return -1
        else:
            return other.l - self.l


def counter(books):
    count = 0
    last = None
    for cur in books:
        if last is None:
            count = 1
            last = cur
        elif last.l > cur.l and last.w > cur.w:
            count += 1
            last = cur
    return count


# [[20, 16], [15, 11], [10, 10], [9, 10]]
def solve_method(input_str):
    input_str = input_str.strip()[2:-2]
    books = []
    for book_str in input_str.split("],["):
        l, w = map(int, book_str.split(","))
        books.append(Book(l, w))    # Book创建一个排序的规则

    books.sort()

    res = counter(books)
    print(res)


if __name__ == '__main__':
    # input_str = sys.stdin.readline()
    input_str = input()
    solve_method(input_str)



