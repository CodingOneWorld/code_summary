# -*- coding: utf-8 -*-
'''
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5

示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4



提示：

    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104


'''
import random


class Solution:
    def findKthLargest(self, nums, k: int) -> int:

        def quick_sort(nums):
            if len(nums)<2:
                return nums
            else:
                # 随机选取划分值，避免最坏情况
                # mid_index=random.randint(0,len(nums))
                # nums[0],nums[mid_index]=nums[mid_index],nums[0]
                mid=nums[0]
                left=[i for i in nums[1:] if i <=mid]
                right=[i for i in nums[1:] if i >mid]
                return quick_sort(left)+[mid]+quick_sort(right)

        return quick_sort(nums)[-k]


nums=[3,2,1,5,6,4]
k = 2
nums=[3,2,3,1,2,4,5,5,6]
k=4
so=Solution()
res=so.findKthLargest(nums,k)
print(res)