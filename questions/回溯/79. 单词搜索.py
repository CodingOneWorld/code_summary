# -*- coding: utf-8 -*-

'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



示例 1：

输入：board = [
["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：

输入：board = [
["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]], word = "SEE"
输出：true

示例 3：

输入：board = [
["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]], word = "ABCB"
输出：false



提示：

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board 和 word 仅由大小写英文字母组成



进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？

https://leetcode.cn/problems/word-search/solutions/2361646/79-dan-ci-sou-suo-hui-su-qing-xi-tu-jie-5yui2/

dfs 递归
'''

class Solution:
    def exist(self, board, word):

        def dfs(i,j,k):
            # 结束条件
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or board[i][j]!=word[k]:
                return False

            if k==len(word)-1:
                return True

            # 操作
            board[i][j]=''
            res=dfs[i-1,j,k+1] or dfs[i,j-1,k+1] or dfs[i+1,j,k+1] or dfs[i,j+1,k+1]
            board[i][j]=word[k]

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False

















class Solution:
    def exist(self, board, word):
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False