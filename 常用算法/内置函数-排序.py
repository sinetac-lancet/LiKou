# -*- coding: utf-8 -*-
# @Time  : 2023/03/26 14:40
# @author: dtf
'''
2、排序
'''
print("======================= 排序 =======================")

'''
# sorted 和 sort(key，reverse=False)区别?
（1）sort()与sorted()的不同在于，sort是在原位重新排列列表，而sorted()是产生一个新的列表。
（2）sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
'''
'''
学习中遇到问题没人解答？小编创建了一个Python学习交流群：711312441
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
list1 = [(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
list1.sort(key=lambda x: x[2])
print(list1)    # [(5, 'Lucy', 19), (8, 'Logan', 20), (2, 'Mike', 22)]


list1 = [(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
list2 = sorted(list1, key=lambda x: x[2])
print(list1)    # [(8, 'Logan', 20), (2, 'Mike', 22), (5, 'Lucy', 19)]
print(list2)    # [(5, 'Lucy', 19), (8, 'Logan', 20), (2, 'Mike', 22)]

'''
倒序
'''
print("======================= 倒序 =======================")
a = [1, 2, 5, 3, 9, 4, 6, 8, 7, 0, 12]
a.sort(reverse=False)
print(a)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]


a = [1, 2, 5, 3, 9, 4, 6, 8, 7, 0, 12]
a.sort(reverse=True)
print(a)    # [12, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]