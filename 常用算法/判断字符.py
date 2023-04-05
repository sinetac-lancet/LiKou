# -*- coding: utf-8 -*-
# @Time  : 2023/04/05 11:15
# @author: dtf

# https://blog.csdn.net/weixin_46507345/article/details/123406895
'''字符串.isalnum() : 判断是否是数字字母的组合，如果包含空格返回False。
字符串.isalpha() :  判断是否是字母，不区分大小写
字符串.isdigit() : 判断是否是数字

字符串.isupper() : 判断是否全部为大写字母
字符串.islower() : 判断是否全部为小写字母
字符串.istitle() : 判断除首字母外全部都是小写'''


str_1 = "123"
str_2 = "Abc"
str_3 = "123Abc"

'''# isdigit函数判断是否数字'''
print("===================isdigit函数判断是否数字===================")
print(str_1.isdigit())
# True
print(str_2.isdigit())
# False
print(str_3.isdigit())
# False

'''
# isalpha判断是否字母
不区分大小写
'''
print("=================isalpha判断是否字母===================")
print(str_1.isalpha())    
# False
print(str_2.isalpha())
# True    
print(str_3.isalpha())    
# False

# 判断汉字的时候
a = "hello我是mis"
print(a.isalpha())
# True
a = "hello"
# True
print(a.isalpha())
a = "hello "
print(a.isalpha())
# False

'''
# isalnum判断是否数字和字母的组合
注意：如果字符串中含有除了字母或者数字之外的字符，比如空格，也会返回Fals
isalnum()必须是数字和字母的混合
'''
print("=================isalnum判断是否数字和字母的组合===================")
print(str_1.isalnum())    
# True
print(str_2.isalnum())
# True
print(str_1.isalnum())    
# True




