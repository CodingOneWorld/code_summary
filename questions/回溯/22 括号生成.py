# -*- coding: utf-8 -*-

'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：

输入：n = 1
输出：["()"]



提示：

    1 <= n <= 8

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans




class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        # 回溯
        def backtrack(S,left,right):
            if len(S)==2*n:
                ans.append(''.join(S))
            if left<n:
                S.append('(')
                backtrack(S,left+1,right)
                S.pop()
            if right<left:
                S.append(')')
                backtrack(S, left,right+1)
                S.pop()

        backtrack([],0,0)

        return ans


































