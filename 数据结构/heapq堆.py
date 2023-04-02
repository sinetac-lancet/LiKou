# -*- coding: utf-8 -*-
# @Time  : 2023/04/02 15:53
# @author: dtf


# 链接：https://blog.csdn.net/aabbccas/article/details/127742912

'''
heapq 库是Python标准库之一，提供了构建小顶堆的方法和一些对小顶堆的基本操作方法(如入堆，出堆等)，可以用于实现堆排序算法。
'''

# heappush(heap,n)数据堆入
import heapq
array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
heap = []
for num in array:
    heapq.heappush(heap, num)
print("array:", array)
print("heap: ", heap)


# heappop(heap)将数组堆中的最小元素弹出
print(heapq.heappop(heap))

# heapify(heap) 将heap属性强制应用到任意一个列表
'''
heapify 函数将使用任意列表作为参数，并且尽可能少的移位操作，将其转化为合法的堆。如果没有建立堆，那么在使用heappush和heappop前应该使用该函数。
'''
heapq.heapify(array)
print("array:", array)

# 获取堆中的最小值或最大值
'''
nlargest(num, heap)，从堆中取出num个数据，从最大的数据开始取，返回结果是一个列表(即使只取一个数据)。如果num大于等于堆中的数据数量，则从大到小取出堆中的所有数据，不会报错，相当于实现了降序排序。
nsmallest(num, heap)，从堆中取出num个数据，从最小的数据开始取，返回结果是一个列表。
'''
array_a = [10, 7, 15, 8]
array_b = [17, 3, 8, 20, 13]
array_merge = heapq.merge(sorted(array_a), sorted(array_b))
print("merge result:", list(array_merge))
