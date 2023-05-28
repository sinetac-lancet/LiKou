# -*- coding: utf-8 -*-
# @Time  : 2023/05/27 11:16
# @author: dtf

'''
HOST收到查询报文，解析出MaxResponseTime字段后，需要在（0，axResponseTime）（s）时间内选取随机时间回应一个响应报文
如果在随机时间收到一个新的查询报文，则会根据两者时间的大小，选取小的一方刷新回应时间

最大响应时间有如下计算方式：
当 MaxRespCode < 128, MaxRespTime = MaxRespCode
当 MaxRespCode >= 128, MaxRespTime = (mant | 0x10) << (exp + 3)
|0|123|4567|
|1|exp|mant|
注：exp最大响应时间的高5-7位；mant位最大响应时间的低4位

输入：
    第一行 查询报文个数C，后续每行为HOST收到报文时间T，及最大响应字段M，以空格分隔
输出：
    Host发送响应报文的时间

输入：
    3
    0 20
    1 10
    8 20
输出：
    11
说明：
    收到3个报文
    1、第0秒收到第1个报文，响应时间为20秒，则要到0+20=20秒响应
    2、第1秒收到第2个报文，响应时间为10秒；则要到1+10=11秒响应，与上面的报文的响应时间比较获得响应时间最小为11秒
    3、第8秒收到第3个报文，响应时间20秒；则要到8+20=28秒响应；与上面的报文的响应时间比较获得响应时间最小为11秒
    最终得到最小响应时间为11秒


'''

'''
最大响应时间有如下计算方式：
当 MaxRespCode < 128, MaxRespTime = MaxRespCode
当 MaxRespCode >= 128, MaxRespTime = (mant | 0x10) << (exp + 3)
|0|123|4567|
|1|exp|mant|
注：exp最大响应时间的高5-7位；mant位最大响应时间的低4位

# =============== 位运算的知识 ==================#
链接：https://blog.csdn.net/weixin_37176244/article/details/116640232
六种位运算
与 &：两个位置上均为1时，结果才是1，否则结果是0
或 ｜：两个位置的结果均为0时，结果才是0
异或 ^：两个位置相同结果为0，不同时结果为1
取反 ～：0变成1，1变成0
左移<<：二进制位全部左移若干位，低位补0填充
右移>>：二进制位全部右移若干位，无符号数高位补0填充

与运算
1）清零
如果想将一个单元清零，即使其全部二进制位为0，只要与一个各位都为零的数值相与，结果为零。
2）取一个数的指定位
比如取数 X=1010 1110 的低4位，只需要另找一个数Y，令Y的低4位为1，其余位为0，即Y=0000 1111，
然后将X与Y进行按位与运算（X&Y=0000 1110）即可得到X的指定位。
3）判断奇偶
只要根据最未位是0还是1来决定，为0就是偶数，为1就是奇数。因此可以用if ((a & 1) == 0)代替if (a % 2 == 0)来判断a是不是偶数。

'''

def calculate_resp_time2(T, M):
    if M >= 128:
        # 0xF = 15；0xF = 7；0x10 = 16
        mant = (M >> 3) & 0xF   # 取一个数的指定位
        exp = M & 0xF           # 取一个数的指定位
        M = (mant | 0x10) << (exp + 3)
    return T + M


def calculate_resp_time(T, M):
    if M >= 128:
        M = float('inf')
    return T + M

C = int(input())
min_resp_time = float("inf")

for _ in range(C):
    T, M = map(int, input().split())
    resp_time = calculate_resp_time(T, M)
    min_resp_time = min(min_resp_time, resp_time)

print(min_resp_time)


