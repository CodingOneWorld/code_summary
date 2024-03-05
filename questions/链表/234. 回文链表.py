# -*- coding: utf-8 -*-
'''
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。



示例 1：

输入：head = [1,2,2,1]
输出：true

示例 2：

输入：head = [1,2]
输出：false



提示：

    链表中节点数目在范围[1, 105] 内
    0 <= Node.val <= 9



进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

https://leetcode.cn/problems/palindrome-linked-list/

https://zhuanlan.zhihu.com/p/556866879?utm_id=0

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针 找中点
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 反转
        cur = slow
        pre = None

        while cur:
            tem = cur.next
            cur.next = pre

            pre = cur
            cur = tem

        # 比较前后链表是否相等
        p1 = head
        p2 = pre
        print(pre.val)

        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True