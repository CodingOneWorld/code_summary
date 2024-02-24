# -*- coding: utf-8 -*-

'''
https://leetcode.cn/problems/subsets/solutions/6899/hui-su-suan-fa-by-powcai-5/

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：

输入：nums = [0]
输出：[[],[0]]



提示：

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    nums 中的所有元素 互不相同

https://leetcode.cn/problems/subsets/description/

https://leetcode.cn/problems/subsets/solutions/71777/hot-100-78zi-ji-python3-hui-su-liang-chong-jie-ti-

'''
class Solution:
    def subsets(self, nums):
        res=[]

        def backtrack(track,index,nums):
            # 结束条件
            if index==len(nums):
                res.append(track[:])
                return

            # 选择
            backtrack(track+[nums[index]],index+1,nums)
            backtrack(track,index+1,nums)

        backtrack([],0,nums)
        return res



class Solution:
    def subsets(self, nums):
        self.res = []
        self.backtrack([], 0, nums)
        return self.res

    def backtrack(self, sol, index, nums):
        if index == len(nums):
            self.res.append(sol)
            return

        self.backtrack(sol + [nums[index]], index + 1, nums)
        self.backtrack(sol, index + 1, nums)


nums=[1,2,3]
so=Solution()
res=so.subsets(nums)
print(res)
