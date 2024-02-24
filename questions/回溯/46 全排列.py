# -*- coding: utf-8 -*-

'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：

输入：nums = [1]
输出：[[1]]



提示：

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    nums 中的所有整数 互不相同


'''

# 回溯法
# 路径 选择列表
# 停止条件 做出选择 回溯 撤销选择

class Solution:
    def permute(self, nums):
        res=[]

        def backtrack(nums,track):

            if len(track)==len(nums):
                res.append(track[:])
                return

            for i in range(len(nums)):

                # 剪枝操作
                if nums[i] in track:
                    continue

                track.append(nums[i])
                backtrack(nums,track)
                track.pop()

        backtrack(nums,[])

        return res


nums = [1,2,3]

so=Solution()
res=so.permute(nums)
print(res)
