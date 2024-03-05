# -*- coding: utf-8 -*-
'''
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。



示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。



提示：

    1 <= nums.length <= 200
    1 <= nums[i] <= 100

https://leetcode.cn/problems/partition-equal-subset-sum/description/

https://leetcode.cn/problems/partition-equal-subset-sum/solutions/663697/416-fen-ge-deng-he-zi-ji-dong-tai-gui-hu-csk5
'''
# test
class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2

        dp=[False]*(len(nums)+1)
        dp[0]=0

        for i in nums:
            for j in range(target,i-1,-1):
                dp[j]=dp[j] or dp[j-i]

        return dp[-1]












class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        print(target)

        # dp数组 dp[j] 和为j的子集是否存在 存在 True  不存在 False
        dp = [False] * (target + 1)
        dp[0] = True

        for i in nums:
            for j in range(target, i - 1, -1):
                dp[j] = dp[j] or dp[j - i]

        return dp[-1]


nums = [1,5,11,5]
so=Solution()
res=so.canPartition(nums)
print(res)



res='0'*5
print(res+'nihao')