# -*- coding: utf-8 -*-
'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”



示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1



提示：

    树中节点数目在范围 [2, 105] 内。
    -109 <= Node.val <= 109
    所有 Node.val 互不相同 。
    p != q
    p 和 q 均存在于给定的二叉树中。


https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

https://blog.csdn.net/weixin_44807903/article/details/133017174
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_father = []
        q_father = []

        def findp(r, path):
            if r.val == p.val:
                p_father.extend(path)
                p_father.append(r)
                return
            if r.left != None:
                path.append(r)
                findp(r.left, path)
                path.pop()
            if r.right != None:
                path.append(r)
                findp(r.right, path)
                path.pop()

        def findq(r, path):
            if r.val == q.val:
                q_father.extend(path)
                q_father.append(r)
                return
            if r.left != None:
                path.append(r)
                findq(r.left, path)
                path.pop()
            if r.right != None:
                path.append(r)
                findq(r.right, path)
                path.pop()

        findp(root, [])
        findq(root, [])
        presult = root
        for i in range(min(len(q_father), len(p_father))):
            if q_father[i] == p_father[i]:
                result = q_father[i]
                continue
            else:
                break
        return result
