# -*- coding: utf-8 -*-

# 层次遍历结果输出到一个列表中
'''
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

输入：root = [3,9,20,null,null,15,7]
输出：[3,9,20,15,7]

示例 2：

输入：root = [1]
输出：[1]

示例 3：

输入：root = []
输出：[]



提示：

    树中节点数目在范围 [0, 2000] 内
    -1000 <= Node.val <= 1000

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]

        queue=[root]
        while queue:
            tem=[]
            for node in queue:
                if node:
                    res.append(node.val)
                    tem.append(node.left)
                    tem.append(node.right)
            queue=tem

        return res
















class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ls=[]
        queue=[root]
        while queue:
            node=queue.pop()
            if not node:
                continue
            ls.append(node.val)

            queue.insert(0,node.left)
            queue.insert(0,node.right)

        return ls