# -*- coding: utf-8 -*-
'''
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。



示例 1：

输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9



提示：

    1 <= n <= 10**4
https://leetcode.cn/problems/perfect-squares/description/


'''


class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化
        dp=[i for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,int(i**0.5)+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
                print(i, j,dp)
        return dp[-1]


# class Solution:
#     def numSquares(self, n: int) -> int:
#         # 动态规划
#         # 初始化
#         # dp[i] i最少由几个平方数加和组成
#         dp=[i for i in range(n+1)]
#
#         for i in range(2,n+1):
#             for j in range(1,int(i**0.5)+1):
#                 dp[i]=min(dp[i],dp[i-j*j]+1)
#         return dp[-1]


n = 12
so=Solution()
res=so.numSquares(n)
print(res)

