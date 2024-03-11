# -*- coding: utf-8 -*-

'''
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

输入：root = [3,9,20,null,null,15,7]
输出：3

示例 2：

输入：root = [1,null,2]
输出：2

'''


# 深度优先遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)

        return max(left,right)+1














class Solution:
    def maxDepth(self, root) -> int:
        if root == None:
            return 0;
        else:
            leftHeight = self.maxDepth(root.left)
            rightHeight = self.maxDepth(root.right)
            return max(leftHeight, rightHeight) + 1
