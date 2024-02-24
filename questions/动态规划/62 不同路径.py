# -*- coding: utf-8 -*-

'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？



示例 1：

输入：m = 3, n = 7
输出：28

示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：

输入：m = 7, n = 3
输出：28

示例 4：

输入：m = 3, n = 3
输出：6
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 0

        dp=[[0]*n]*m

        dp[0][0]=0
        dp[0][1]=1
        dp[1][0]=1

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = 0
                if i==0:
                    if j==0:
                        dp[i][j] = 0
                    if j==1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j - 1]
                elif j==0:
                    if i==1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]


        return dp[m-1][n-1]

m=3
n=7
so=Solution()
res=so.uniquePaths(3,7)
print(res)