
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 解析两个数字
        # 解析两个数字
        nums1 = []
        while l1:
            nums1.append(l1.val)
            l1 = l1.next

        num1 = 0
        for i in range(len(nums1)):
            num1 += nums1[i] * 10 ** i

        nums2 = []
        while l2:
            nums2.append(l2.val)
            l2 = l2.next

        num2 = 0
        for i in range(len(nums2)):
            num2 += nums2[i] * 10 ** i

        num3 = num1 + num2

        nums3 = list(str(num3))
        nums3.reverse()

        l3 = p = ListNode(0)
        for i in range(len(nums3)):
            node = ListNode(int(nums3[i]))
            p.next = node
            p = node
        p.next = None

        return l3.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=l1
        anum1=[]
        while head!=None:
            num=head.val
            anum1.append(num)
            head=head.next
        len1 = len(anum1)
        num1 = 0
        for i in range(len1):
            base = i
            num1 = num1 + anum1[i] * pow(10, base)
        print(num1)
        head = l2
        anum2 = []
        while head != None:
            num = head.val
            anum2.append(num)
            head = head.next
        len2 = len(anum2)
        num2 = 0
        for i in range(len2):
            base = i
            num2 = num2 + anum2[i] * pow(10, base)
        print(num2)

        num = [int(i) for i in list(str(num1 + num2))]
        num3 = []
        for i in range(len(num)):
            num3.append(num[len(num) - 1 - i])
        print(num3)

        head=ListNode()
        p = head
        for i in range(len(num3)):
            p.val=num3[i]
            if i==len(num3)-1:
                p.next=None
                break
            temp=ListNode()
            p.next=temp
            p=temp
        return head


l1=ListNode()
ll2=ListNode()
ll3=ListNode()
l1.val=2
l1.next=ll2
ll2.val=4
ll2.next=ll3
ll3.val=3
ll3.next=None
# print(l1.val)

l2=ListNode()
ll2=ListNode()
ll3=ListNode()
l2.val=5
l2.next=ll2
ll2.val=6
ll2.next=ll3
ll3.val=4
ll3.next=None
# print(l2.val)


so=Solution()
p=so.addTwoNumbers(l1,l2)
print(p.val)
print(p.next.val)
print(p.next.next.val)
print(p.next.next.next.val)



















# 列表解法
class Solution:
    def addTwoNumbers(self, l1, l2):
        len1=len(l1)
        len2=len(l2)
        # if len1==1 and len2==1:
        #     return [int(i) for i in list(str(l1[0]+l2[0]))]
        num1=0
        for i in range(len1):
            base=i
            num1=num1+l1[i]*pow(10,base)
        print(num1)
        num2 = 0
        for i in range(len2):
            base = i
            num2 = num2 + l2[i] * pow(10, base)
        print(num2)

        num=[int(i) for i in list(str(num1+num2))]
        num3=[]
        for i in range(len(num)):
            num3.append(num[len(num)-1-i])
        print(num3)
        return num3

# l1 = [2,4,3]
# l2 = [5,6,4]
# so=Solution()
# so.addTwoNumbers(l1,l2)