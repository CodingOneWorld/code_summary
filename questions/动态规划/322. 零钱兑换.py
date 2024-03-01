# -*- coding: utf-8 -*-
'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：

输入：coins = [2], amount = 3
输出：-1

示例 3：

输入：coins = [1], amount = 0
输出：0



提示：

    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104

https://leetcode.cn/problems/coin-change/


动态规划
选择DP
'''

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount==0:
            return 0

        # dp
        dp=[amount+1]*(amount+1)

        for i in range(1,amount+1):
            for coin in coins:
                if coin<i:
                    dp[i]=min(dp[i],dp[i-coin]+1)

        return -1 if dp[amount+1]==amount+1 else dp[amount]












class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount==0:
            return 0

        # dp[i] 凑成金额i最少需要多少个硬币

        # 初始化
        # dp=[i for i in range(amount+1)]
        dp=[amount+1]*(amount+1)

        for i in range(1,amount+1):
            for coin in coins:
                if i>coin:
                    dp[i]=min(dp[i],dp[i-coin]+1)

        return -1 if dp[amount]==amount+1 else dp[amount]



class Solution:
    def coinChange(self, coins, amount: int) -> int:
        '''
        动态规划
        子问题定义：dp[i] 金额i最少由dp[i]个硬币组成
        状态转移方程：dp[i]=argmin coin dp[i-cion] +1
        '''

        dp=[amount+1]*(amount+1)
        dp[0]=0

        for i in range(1,amount+1):
            for j in coins:
                if j >i:
                    continue
                dp[i]=min(dp[i],dp[i-j]+1)
            print(dp)

        return -1 if (dp[amount] == amount + 1) else dp[amount]

        # 优化
        dp = [amount + 1] * (amount + 1)  # 初始化为一个较大的值，如 +inf 或 amount+1
        dp[0] = 0  # 合法的初始化；其他 dp[j]均不合法

        # 完全背包：优化后的状态转移
        for coin in coins:  # 第一层循环：遍历硬币
            for j in range(coin, amount + 1):  # 第二层循环：遍历背包【正序】
                dp[j] = min(dp[j], dp[j - coin] + 1)  # 可选择当前硬币

        ans = dp[amount]
        return ans if ans != amount + 1 else -1




coins = [1, 2, 5]
amount = 11
so=Solution()
res=so.coinChange(coins,amount)
print(res)



def coinChange(coins, amount: int) -> int:
    # 最优子结构  状态转移
    # dp[i] 金额i最少需要的硬币个数
    # 初始值 每个金额最多由他本身数目的个数组成
    dp=[i for i in range(amount+1)]
    dp[0]=0
    for i in range(amount+1):
        for coin in coins:
            if i-coin<0:
                continue
            dp[i]=min(dp[i],dp[i-coin]+1)
    return dp[-1]

coins = [1, 2, 5]
amount = 11
res=coinChange(coins,amount)
print(res)
