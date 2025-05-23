# -*- coding: utf-8 -*-

'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。



示例 1：

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：

输入：head = [1,2]
输出：[2,1]

示例 3：

输入：head = []
输出：[]



提示：

    链表中节点的数目范围是 [0, 5000]
    -5000 <= Node.val <= 5000



进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

https://blog.csdn.net/ZhouXin1111112/article/details/132586044

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None
        while cur:
            tem = cur.next
            cur.next = pre

            pre = cur
            cur = tem
        return pre
