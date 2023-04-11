# -*- coding: utf-8 -*-
# @Time  : 2023/04/11 20:53
# @author: dtf


# https://blog.csdn.net/weixin_44799217/article/details/124380270
'''
注意：使用dict[key]=value时，若key不存在则报错；使用dict.get(key)时，若key不存在则会返回一个默认值。
defaultdict接受一个工厂函数作为参数，如下来构造：
        dict =defaultdict(factory_function)
factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[]，str对应的是空字符串，set对应set()，int对应0。
defaultdict是python内建dict类的一个字类，功能与dict相同，但它带有一个默认的值，若key值不存在时返回一个默认的值。
示例代码：
'''
print("====================== setdefault ====================")
lst = ['A', 'B', 'C', 'D', 'e']
dic = {}

for i in lst:
    dic.setdefault(i, 0)
    dic[i] += 1
print(dic)

'''
二、setdefault()和defaultdict()的区别：
setdefault()是字典的一个实例方法，接收两个参数，用法和字典的get()方法相似，但是比get()方法更加强大。都为字典的key设置一个默认值。
二者的区别是：get 方法设置的默认值不会改变原字典， 而setdefault设置的默认值会改变原字典的值。
'''
print("====================== setdefault()和defaultdict()的区别 ====================")
dic1 = {"A": "a", "B": "b"}
x = dic1.get("E", "e")
print(x)
print(dic1)

dic2 = {"C": "c", "D": "d"}
y = dic2.setdefault("E", 'e')
print(y)
print(dic2)


'''
defaultdict()
    是属于collections 模块下的一个工厂函数，用于构建字典对象，接收一个函数（可调用）对象为作为参数。参数返回的类型是什么，key对应value就是什么类型。
'''
print("====================== defaultdict() ====================")
from collections import defaultdict

lst = [("A", "1"), ("B", "1"), ("A", "2"), ("B", "2"), ("A", "3"), ("B", "3")]
dic = defaultdict(list)
print(dic)
for key, value in lst:
    dic[key].append(value)
print(dic)
print(type(dic))
for key, value in dic.items():
    print(key, value)

