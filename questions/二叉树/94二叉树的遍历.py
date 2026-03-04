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

# 中序的迭代解法
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        stack = list()

        while root or stack:
            # 步骤1：一直向左走，压入栈
            while root:
                stack.append(root)
                root = root.left
            # 步骤2：左子树已处理，弹出栈顶
            root = stack.pop()
            res.append(root.val)
            # 步骤3：处理右子树
            root = root.right
        return res

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