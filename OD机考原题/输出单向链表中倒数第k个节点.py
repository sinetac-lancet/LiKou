# -*- coding: utf-8 -*-
# @Time  : 2023/04/10 22:37
# @author: dtf

class Node(object):

    def __init__(self, val=0):
        self.val = val
        self.next = None


while True:
    try:
        l, s, k, head = int(input()), list(map(int, input().split())), int(input()), Node()
        while k:
            head.next = Node(s.pop())
            head = head.next
            k -= 1
        print(head.val)
    except:
        break