# -*- coding: utf-8 -*-
# @Time  : 2023/05/25 20:57
# @author: dtf

'''
多组整数数组，需要将他们合并成一个新的数组
合并规则：
    从每个数组里按顺序取出固定长度的内容合并到新的数组中，取完的内容会被删掉
    如果该行不足固定长度或者已经为空，则直接取出剩余部分的内容放到新的数组中，继续下一行

输入：
    第一行是 每次读取固定长度，0<长度<10；
    第二行是整数数组的数目0<数目<1000；
    第3~n行是需要合并的数组，不同的数组用回车换行分隔
    数组内部用逗号分隔

    最大不超过100个元素
输出：
    输出一个新的数组，用逗号分隔
3
2
2,5,6,7,9,5,7
1,7,4,3,4

2,5,6,1,7,4,7,9,5,3,4,7


4
3
1,2,3,4,5,6
1,2,3
1,2,3,4

1,2,3,4,1,2,3,1,2,3,4,5,6

'''
import copy

def method(k, n, data):
    build = ""
    index = 0
    # 使用一个while循环遍历整数列表的每一行，并从列表的开头取出k个整数，
    # 并将其附加到字符串构建器中
    while len(data) > 0:
        print('data: ', data)
        '''利用拷贝的相关知识'''
        sub_list = data[index]  # 得到每一行整数数组
        print('浅拷贝sub_list: ', sub_list)
        # 取出k个整数
        for i in range(k):
            if len(sub_list) == 0:  # 该行的整数数组已经被完全取出
                data.pop(index)     # 在原数据中删除该行
                index -= 1          # 计数-1
                break
            build += str(sub_list.pop(0)) + ','
        index += 1
        '''遍历了所有行，然后置0，重新开始循环'''
        if index >= len(data):
            index = 0
    return build[:-1]


if __name__ == '__main__':
    k = int(input().strip())
    n = int(input().strip())
    data = [list(map(int, input().split(','))) for _ in range(n)]
    res = method(k, n, data)
    print(res)
