# -*- coding: utf-8 -*-

'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


示例 1：

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：

输入：l1 = [], l2 = []
输出：[]

示例 3：

输入：l1 = [], l2 = [0]
输出：[0]



提示：

    两个链表的节点数目范围是 [0, 50]
    -100 <= Node.val <= 100
    l1 和 l2 均按 非递减顺序 排列


'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def fun(self,l1,l2):
        res=cur=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 if l1 else l2
        return res.next


# 构造链表
l1=head1=ListNode(0)
for i in [1,2,4]:
    p=ListNode(i)
    l1.next=p
    l1=l1.next
head1=head1.next
print(head1.val)

l2=head2=ListNode(0)
for i in [1,3,4]:
    p=ListNode(i)
    l2.next=p
    l2=l2.next
head2=head2.next
print(head2.val)

so=Solution()
ll=so.fun(head1,head2)
while ll:
    print(ll.val)
    ll=ll.next














# class Solution:
#     def mergeTwoLists(self, list1, list2):
#         res=cur=ListNode(0)
#         while list1 and list2:
#             if list1.val < list2.val:
#                 cur.next,list1=list1,list1.next
#             else:
#                 cur.next,list2=list2,list2.next
#             cur=cur.next
#         cur.next=list1 if list1 else list2
#
#         return res.next
#
#
#
#
#
#
#
#
#
#
#
# class Solution:
#     def mergeTwoLists(self, list1, list2):
#         cur = res = ListNode(0)
#         while list1 and list2:
#             if list1.val < list2.val:
#                 cur.next, list1 = list1, list1.next
#             else:
#                 cur.next, list2 = list2, list2.next
#             cur = cur.next
#         cur.next = list1 if list1 else list2
#         return res.next
#
# l1=ListNode(1)
# l1.next=ListNode(2)
# l1.next.next=ListNode(4)
#
# l2=ListNode(1)
# l2.next=ListNode(3)
# l2.next.next=ListNode(4)