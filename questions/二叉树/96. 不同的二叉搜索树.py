# -*- coding: utf-8 -*-

'''
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

https://leetcode.cn/problems/unique-binary-search-trees/solutions/331743/er-cha-sou-suo-shu-fu-xi-li-zi-jie-shi-si-lu-by-xi/

找规律
动态规划
'''

class Solution:
    def numTrees(self, n: int) -> int:
        store = [1, 1]  # f(0),f(1)
        if n <= 1:
            return store[n]
        for m in range(2, n + 1):
            s = m - 1
            count = 0
            for i in range(m):
                count += store[i] * store[s - i]
            store.append(count)
        return store[n]

