# -*- coding: utf-8 -*-

'''
给你一个二叉树的根节点 root ， 检查它是否轴对称。

https://leetcode.cn/problems/symmetric-tree/solutions/2361627/101-dui-cheng-er-cha-shu-fen-zhi-qing-xi-8oba/

思路：
递归
判断根节点的左右子树保持对称

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def recur(left,right):
            # 递归终止条件
            if not left and not right:
                return True
            if not left or not right or left.val!=right.val:
                return False

            return recur(left.left,right.right) and recur(left.right,right.left)

        return recur(root.left,root.right)














class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return not root or recur(root.left, root.right)