# -*- coding: utf-8 -*-

'''
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

示例 2:

输入: preorder = [-1], inorder = [-1]
输出: [-1]



提示:

    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder 和 inorder 均 无重复 元素
    inorder 均出现在 preorder
    preorder 保证 为二叉树的前序遍历序列
    inorder 保证 为二叉树的中序遍历序列

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:  # 递归终止条件
            return
        root = TreeNode(preorder[0])  # 先序为“根左右”，所以根据preorder可以确定root
        idx = inorder.index(preorder[0])  # 中序为“左根右”，根据root可以划分出左右子树
        # 下面递归对root的左右子树求解即可
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root


# 递归  终止条件 每次递归需要做的逻辑
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        root=TreeNode(preorder[0])   # 在先序遍历中找到根节点
        idx=inorder.index(preorder[0])  # 找到根节点在中序遍历中的索引

        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root