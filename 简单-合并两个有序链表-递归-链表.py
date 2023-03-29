# -*- coding: utf-8 -*-
# @Time  : 2023/03/25 21:29
# @author: dtf


# https://leetcode.cn/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/
# https://leetcode.cn/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/
'''
拓展：如何计算递归的时间复杂度和空间复杂度呢？
给出一个递归算法，其时间复杂度 O(T) 通常是递归调用的数量（记作 R） 和计算的时间复杂度的乘积（表示为 O(s)）的乘积：O(T)=R∗O(s)


'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, L1: ListNode, L2: ListNode) -> ListNode:
        if L1 is None:
            return L2
        elif L2 is None:
            return L1
        elif L1.val < L2.val:
            L1.next = self.mergeTwoLists(L1.next, L2)
            return L1
        else:
            L2.next = self.mergeTwoLists(L2.next, L1)
            return L2


if __name__ == '__main__':
    l1 = [1, 2, 4]
    for i in l1:
        L1 = ListNode(i)
    l2 = [1, 3, 4]
    for i in l2:
        L2 = ListNode(i)
    sl = Solution()
    print(sl.mergeTwoLists(l1, l2))