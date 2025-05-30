# -*- coding: utf-8 -*-

'''
https://leetcode.cn/problems/sort-list/

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。



示例 1：

输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：

输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：

输入：head = []
输出：[]



提示：

    链表中节点的数目在范围 [0, 5 * 104] 内
    -105 <= Node.val <= 105



进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

https://leetcode.cn/problems/sort-list/description/

'''

# https://blog.csdn.net/lht0909/article/details/124225162

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 特殊判断
        if not head or not head.next: return head

        # 寻找链表的中部，并切分
        fast,slow=head.next,head
        while fast and fast.next:
            fast,slow=fast.next.next,slow.next
        mid,slow.next=slow.next,None

        # 递归
        left,right=self.sortList(head),self.sortList(mid)

        # 合并有序链表
        cur=res=ListNode(0)
        while left and right:
            if left.val <right.val:
                cur.next,left=left,left.next
            else:
                cur.next,right=right,right.next
            cur=cur.next
        cur.next=left if left else right

        return res.next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next