# -*- coding: utf-8 -*-

'''
给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



示例 1:

输入: prices = [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

示例 2:

输入: prices = [1]
输出: 0



提示：

    1 <= prices.length <= 5000
    0 <= prices[i] <= 1000

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/


动态规划
状态DP

'''



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        empty,empty_freeze,hold=0,0,-prices[0]
        for i in range(1,len(prices)):
            empty0=max(empty,empty_freeze)
            empty_freeze0=hold+prices[i]
            hold0=max(empty-prices[i],hold)
            empty, empty_freeze, hold = empty0, empty_freeze0, hold0
        return max(empty,empty_freeze,hold)








class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # 状态初始化
        # 有三种不同的状态  空仓可购买  空仓不可购买（刚卖出）  持仓

        empty,empty_freeze,hold=0,0,-prices[0]

        for i in range(1,len(prices)):
            # 状态的转化，从之前价格的状态转移到当前价格的可能状态
            empty0=max(empty,empty_freeze)
            empty_freeze0=hold+prices[i]
            hold0=max(empty - prices[i], hold)
            empty, empty_freeze, hold=empty0,empty_freeze0,hold0
        return max(empty, empty_freeze)

