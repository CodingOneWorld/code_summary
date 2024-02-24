# -*- coding: utf-8 -*-

'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。



示例 1：

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：

输入：head = [1], n = 1
输出：[]

示例 3：

输入：head = [1,2], n = 1
输出：[1]



提示：

    链表中结点的数目为 sz
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz



进阶：你能尝试使用一趟扫描实现吗？
'''

from Cython.Compiler.ExprNodes import ListNode
# from numba import Optional

# Definition for singly-linked list.
class Node():                  #value + next
    def __init__(self, value = None, next = None):
        self._value = value
        self._next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head=ListNode()
head.next=ListNode(1)
# head.next.next=ListNode(2)




class Solution:
    def removeNthFromEnd(self, head, n: int):
        # 得到链表的结点数
        sz=1
        p=head
        while p.next !=None:
            sz+=1
            p=p.next

        # 计算要删除的结点是正数第几个结点
        an=sz-n+1
        print(an)

        # 删除第an个结点
        if an==1:
            if sz>1:
                p = head
                return p.next
            else:
                return None
        else:
            p=head
            count=1
            while p.next!=None and count<(an-1):
                count+=1
                p=p.next

            # 删除
            p.next=p.next.next

        return head

so=Solution()
res=so.removeNthFromEnd(head,2)
print(res.val)

