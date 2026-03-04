'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。



示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：

输入：nums = [], target = 0
输出：[-1,-1]



提示：

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums 是一个非递减数组
    -109 <= target <= 109

'''


# 循环查找，O(n)解法
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=-1
        r=-1
        tag=0

        for i in range(len(nums)):
            if nums[i]==target and tag==0:
                l=i
                tag=1
            if nums[i]==target and tag==1:
                r=i
        return [l,r]

# 二分查找
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # 基础二分查找 左闭右开区间
        def binarySearch(nums, target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        start = binarySearch(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = binarySearch(nums, target + 1) - 1
        return [start, end]
