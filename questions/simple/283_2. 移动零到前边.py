# -*- coding: utf-8 -*-
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。



示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:

输入: nums = [0]
输出: [0]



提示:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1



进阶：你能尽量减少完成的操作次数吗？

https://leetcode.cn/problems/move-zeroes/
'''



# 移动零
# 借助临时数组解法
class Solution:
    def moveZeroes(self, nums) -> None:
        tem=[]
        for num in nums:
            if num:
                tem.append(num)

        for i in range(len(nums)):
            if i <len(nums)-len(tem):
                nums[i]=0
            else:
                nums[i]=tem[i-len(nums)+len(tem)]

# 第一次遇到非零元素，将非零元素与数组nums[0]互换，第二次遇到非零元素，将非零元素与nums[1]互换，第三次遇到非零元素，将非零元素与nums[2]，以此类推，直到遍历完数组
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
                :type nums: List[int]
                :rtype: None Do not return anything, modify nums in-place instead.
                """
        left = 0  # 第一个指针，left
        for right in range(len(nums)):  # 第二个指针，right，在for循环中实现移动
            # 核心的交换步骤：如果当前right为0，则交换到左侧，把0往左侧移动就对了
            if not nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1  # 交换后也移动left


nums=[0,1,0,3,12]
nums=[0,1,0,3,12,0,0,0]
so=Solution()
so.moveZeroes(nums)
print(nums)