# -*- coding: utf-8 -*-

'''

https://leetcode.cn/problems/majority-element/solutions/2362000/169-duo-shu-yuan-su-mo-er-tou-piao-qing-ledrh/

给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1：

输入：nums = [3,2,3]
输出：3

示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2


提示：

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109



进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

https://leetcode.cn/problems/majority-element/solutions/15585/qiu-zhong-shu-python3pai-xu-fa-by-pandawakaka/

'''

# 计数法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set1 = set(nums)
        for i in set1:
            if nums.count(i) > (len(nums) // 2):
                return i

# 哈希表
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        set1 = set(nums)
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        for i in set1:
            if dic.get(i)>(len(nums)//2):
                return i

# 排序法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

# 摩尔投票
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x



