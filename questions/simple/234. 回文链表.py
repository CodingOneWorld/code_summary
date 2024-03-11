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
        # 中间切分
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        # 反转后半部分
        cur,pre=slow,None
        while cur:
            tem=cur.next
            cur.next=pre

            pre=cur
            cur=tem
        # 比较前后部分
        p1=head
        p2=pre
        while p1 and p2:
            if p1.val !=p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True



















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


















class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. 先用快慢指针找到后半部分
        fast = head
        slow = head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        # 此时慢指针就指向后半部分的头结点
        #（如果链表结点数是奇数，那么此时必定是正中间结点的后一个）

        # 2. 翻转后半部分
        # slow = Solution.reverse_list(slow)
        cur, pre = slow, None

        while cur:
            tem = cur.next
            cur.next = pre

            pre = cur
            cur = tem
        slow=pre

        # 3. 对比前后是否相等即可
        l = head
        r = slow
        while l and r:
            # 如果值不相等，则必定不是回文链表，直接返回 false
            if l.val != r.val:
                return False

            # 如果值相等，则都移动至下一个结点继续对比
            l = l.next
            r = r.next

        # 所有值都相等，则是回文链表
        return True

    @staticmethod
    def reverse_list(head):
        cur,pre=head,None

        while cur:
            tem=cur.next
            cur.next=pre

            pre=cur
            cur=tem
        return pre