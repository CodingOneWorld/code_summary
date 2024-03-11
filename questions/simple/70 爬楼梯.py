# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/climbing-stairs/solutions/2361764/70-pa-lou-ti-dong-tai-gui-hua-qing-xi-tu-ruwa/

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？



示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶



提示：

    1 <= n <= 45


"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2

        fb1=1
        fb2=2

        for i in range(2,n):
            fb2=fb1+fb2
            fb1=fb2

        return fb2







# 动态规划
# 重叠子问题
# 最优子结构
# 状态转移方程
# f(n)=f(n-1)+f(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        fb1=1
        fb2=2
        for i in range(3,n+1):
            fb1,fb2=fb2,fb1+fb2
        return fb2

