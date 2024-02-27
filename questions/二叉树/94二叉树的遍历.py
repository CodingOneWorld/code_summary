# -*- coding: utf-8 -*-

'''
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 中序
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []

        def dfs(node):
            if node != None:
                dfs(node.left)
                l.append(node.val)
                dfs(node.right)

        dfs(root)

        return l

    # 前序
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []

        def dfs(node):
            if node != None:
                l.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        return l

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []

        def dfs(node):
            if node != None:
                dfs(node.left)
                dfs(node.right)
                l.append(node.val)

        dfs(root)

        return l