# -*- coding: utf-8 -*-
# @Time  : 2023/04/11 21:22
# @author: dtf


# https://blog.csdn.net/qq_62799602/article/details/126843864



'''
sort 和 sorted 分别对字典进行排序的操作：

'''
print("============ sort 和 sorted 分别对字典进行排序的操作：==============")
print("==========sort() =============")
# 要求：将四个人按照年龄从小到大依次输出
d = {'张三': 23, '李四': 18, '王五': 20, '刘六': 25}
ls = list(d.items()) # 将键值对以元组的形式存放，最后保存在一个列表中
# ls = [('张三', 23), ('李四', 18), ('王五', 20), ('刘六', 25)]
ls.sort(key=lambda x: x[1], reverse=True)
print(ls)   # 运行结果为 [('刘六', 25), ('张三', 23), ('王五', 20), ('李四', 18)]

print("==========sorted() =============")
d = {'张三': 23, '李四': 18, '王五': 20, '刘六': 25}
print(d.items())
print(d.values())
aa = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(aa)   # 运行结果为 [('刘六', 25), ('张三', 23), ('王五', 20), ('李四', 18)]

'''
拓展
'''
print("\n求得字典最大值所对应的键和值：（sorted）")
ans = min(d.items(), key=lambda x: x[1])
# 运行结果为 年龄最小的人为"李四":18岁
print('年龄最小的人为"{}":{}岁'.format(ans[0], ans[1]))

'''
多重条件
'''