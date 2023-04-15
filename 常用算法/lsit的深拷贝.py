# -*- coding: utf-8 -*-
# @Time  : 2023/04/15 17:40
# @author: dtf



# https://blog.csdn.net/weixin_42521185/article/details/124292157

'''
二、奇怪的事情
x = [1, 2, 3]
y = []
y.append(x)
x.append(9)
y.append(x)
print(y)

>>>[[1, 2, 3, 9], [1, 2, 3, 9]]

三、解释原因
当list类型的对象进行append()操作时，实际上追加的数据是该对象的引用。 因此可以看做是一个“浅拷贝”
如果要得到预期结果，应该写成深拷贝。
import copy
x = [1, 2, 3]
y = []
y.append(copy.deepcopy(x))
x.append(9)
y.append(copy.deepcopy(x))
print(y)

>>> [[1, 2, 3], [1, 2, 3, 9]]
'''