# -*- coding: utf-8 -*-
# @Time  : 2023/05/27 9:10
# @author: dtf
'''
https://blog.csdn.net/hihell/article/details/130816521
两门选修课，每门都有一部分学生选修，需要找出同时选修两门课的同学，先按照班级进行划分，
班级编号小的先输出，每个班级按照两门选修课成绩和 的降序排序，成绩相同时按照学生的学号升序排序

输入：
    第一行 第一门选修课学生成绩
    第二行 第二门选修课学生成绩
    每行数据中学生之间以英文分号’;‘分隔，每个学生的学号和成绩之间以英文逗号','分隔
    学号格式为8位数字（2位院系编号+入学年份后2位+院系内部1位专业编号+所在班级3位学号）
    学生成绩为0-100之间的整数，两门选修课选修学生数的取值范围为1-2000之间的整数
输出：
    同时选修了两门选修课的学生的学号，如果没有则输出NULL
    1、先按照班级编号小的先输出，每个班级先输出班级编号（学号前五位），然后另起一行输出这个班级同时选修两门课的学生学号
    2、学号按照两门选修课成绩和 的降序排序，成绩相同时按照学生的学号升序排序

01202021,75;01201033,95;01202008,80;01203006,90;01203088,100
01202008,70;01203088,85;01202111,80;01202021,75;01201100,88

01202
01202008;01202021
01203
01203088
'''

'''
字典，键为班级号，键值为列表存放[[学号，两门选修课成绩和]]
'''
# from collections import defaultdict
#
#
# def main():
#     data1 = input().split(';')
#     data2 = input().split(';')
#
#     data_dict = defaultdict(list)
#     dic1 = {}
#     for d1 in data1:
#         key, val = d1.split(',')
#         dic1[key] = val
#     dic2 = {}
#     for d2 in data2:
#         key, val = d2.split(',')
#         dic2[key] = val
#     for key in dic1.keys():
#         if key in dic2.keys():
#             sums = int(dic1[key]) + int(dic2[key])
#             key2 = key[:5]
#             data_dict[key2].append((key, sums))
#     print(data_dict)
#     for key, val in data_dict.items():
#         val.sort(key=lambda x: (-x[1], x[0]))
#         data_dict[key] = val
#     '''
#     小技巧，如何对字典键进行排序
#     '''
#     for key in sorted(data_dict.keys()):
#         print(key)

#
# if __name__ == '__main__':
#     main()



# 改进
from collections import defaultdict
import sys


class Student:
    def __init__(self, id, score):
        self.id = id
        self.score = score

    def __lt__(self, other):
        if self.score == other.score:
            return self.id < other.id       # 根据学号升序
        return self.score > other.score     # 根据成绩和降序


def main():
    one = input().split(";")
    two = input().split(";")
    t_ids = {}
    for t in two:
        t_stu = t.split(",")
        t_id = t_stu[0]
        t_score = int(t_stu[1])
        t_ids[t_id] = t_score

    map = defaultdict(set)
    for s in one:
        s_stu = s.split(",")
        s_id = s_stu[0]
        if s_id in t_ids:
            s_score = int(s_stu[1])
            t_score = t_ids[s_id]
            total_score = s_score + t_score
            cls = s_id[:5]
            student = Student(s_id, total_score)
            map[cls].add(student)
    print(map)
    if not map:
        print("NULL")
    else:
        for key in sorted(map.keys()):  # 键：班级号；按照班级号升序
            value = sorted(map[key])    #
            print(key)
            print(";".join([student.id for student in value]))


if __name__ == "__main__":
    main()

