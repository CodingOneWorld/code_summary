# -*- coding: utf-8 -*-
'''
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。



示例 1：

输入：nums = [1,3,4,2,2]
输出：2

示例 2：

输入：nums = [3,1,3,4,2]
输出：3



提示：

    1 <= n <= 105
    nums.length == n + 1
    1 <= nums[i] <= n
    nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次



进阶：

    如何证明 nums 中至少存在一个重复的数字?
    你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？

https://leetcode.cn/problems/find-the-duplicate-number/

二分查找

按题目表达，设数组长度为n，则数组中元素∈[1,n−1]，且只有一个重复元素。一个直观的想法，设一个数字k∈[1,n−1]，统计数组中小于等于k的数字的个数count：

    若count<=k，说明重复数字一定在(k,n−1]的范围内。
    若count>k，说明重复数字一定在[0,k]的范围内。

利用这个性质，我们使用二分查找逐渐缩小重复数字所在的范围。

    初试化左右 数字 边界left=1,right=n−1
    循环条件left<right:
        mid=(left+right)//2
        按照性质，统计数组中小于等于midmidmid的元素个数countcountcount
        若 count<=mid，说明重复数字一定在(mid,right]的范围内。令left=mid+1
        若count>mid，说明重复数字一定在[left,mid]的范围内。令right=mid
    返回leftleftleft

'''
class Solution:
    def findDuplicate(self, nums) -> int:
        left=1
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            # 计算小于等于mid的数量count
            # count<=mid 在右边
            # count>mid 在左边
            count=0
            for num in nums:
                if num<=mid:
                    count+=1
            if count<=mid:
                left = mid + 1
            else:
                right = mid
        return left