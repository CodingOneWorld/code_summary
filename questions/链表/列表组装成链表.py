'''
给定一个列表 nums=[1,2,3,4,5]  将他组装为链表
'''

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None


class Solution:
    def fun(self,nums):
        head=pre=ListNode(nums[0])
        for i in range(1,len(nums)):
            cur=ListNode(nums[i])
            pre.next=cur

            pre=cur
        return head

nums=[1,2,3,4,5]
so=Solution()
head=so.fun(nums)
print(head.val)

# 链表遍历
while head:
    print(head.val)
    head=head.next