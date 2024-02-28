# -*- coding: utf-8 -*-

'''
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

子数组 是数组的连续子序列。



示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。



提示:

    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数

'''

# https://blog.csdn.net/weixin_44807903/article/details/130936604

class Solution:
    def maxProduct(self, nums) -> int:
        max_v=[nums[0]]
        min_v=[nums[0]]

        for i in range(1,len(nums)):
            max_v.append(max(max_v[i-1]*nums[i],nums[i],min_v[i-1]*nums[i]))
            min_v.append(min(max_v[i-1]*nums[i],nums[i],min_v[i-1]*nums[i]))

        return max(max_v)

# 优化存储空间
class Solution:
    def maxProduct(self, nums) -> int:
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res
