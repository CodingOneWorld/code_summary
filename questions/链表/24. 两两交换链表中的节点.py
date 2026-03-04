'''
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：

输入：head = []
输出：[]

示例 3：

输入：head = [1]
输出：[1]

提示：

    链表中节点的数目在范围 [0, 100] 内
    0 <= Node.val <= 100

'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        p = ListNode(-1)
        # 用stack保存每次迭代的两个节点
        # head指向新的p节点，函数结束时返回head.next即可
        cur, head, stack = head, p, []
        while cur and cur.next:
            # 将两个节点放入stack中
            stack.append(cur)
            stack.append(cur.next)
            # 当前节点往前走两步
            cur = cur.next.next
            # 从stack中弹出两个节点，然后用p节点指向新弹出的两个节点
            p.next = stack.pop()
            p.next.next = stack.pop()
            p = p.next.next
        # 注意边界条件，当链表长度是奇数时，cur就不为空
        if cur:
            p.next = cur
        else:
            p.next = None
        return head.next
