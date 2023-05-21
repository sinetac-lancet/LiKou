# -*- coding: utf-8 -*-
# @Time  : 2023/05/20 16:35
# @author: dtf


# https://dream.blog.csdn.net/article/details/128985575

'''
输入：
    head add x 表示从头部添加数据x，
    tail add x 表示从尾部添加数据x
    remove 表示移除一个数据，要求移除数据的顺序为1 到 n
    为了满足要求，需要可以时刻调整列表中的数据顺序
输出：

'''

from collections import deque


def solve_method(commands):
    times = 0
    in_ = 0
    out = 0
    linked_list = deque()

    for command in commands:
        c = command[0]
        if c == 'h':    # 按照指定位置，记录是第几次添加数据
            linked_list.appendleft(in_ + 1)
            in_ += 1
        elif c == 't':  # 按照指定位置，记录是第几次添加数据
            linked_list.append(in_ + 1)
            in_ += 1
        else:   # 移除数据
            # 为了满足要求：移除数据的顺序为1 到 n
            # 因此需要时刻更新数据的顺序
            # linked_list是一个升序的队列，因此linked_list[0]是最左边的元素
            if linked_list[0] != out + 1:
                times += 1
                linked_list = deque(sorted(linked_list))

            linked_list.popleft()
            out += 1    # 记录移除元素个数

    return times


n = int(input().strip())
commands = [input().strip() for i in range(n * 2)]
res = solve_method(commands)
print(res)
