# -*- coding: utf-8 -*-

'''
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 target 的不同组合数少于 150 个。



示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：

输入: candidates = [2], target = 1
输出: []



提示：

    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    candidates 的所有元素 互不相同
    1 <= target <= 40


'''

# 感觉是回溯法
# 回溯法要诀    路径  选择列表   停止条件
from _ast import List

class Solution:
    def combinationSum(self, candidates, target):
        res=[]

        def backtrack(nums,track):
            # 结束条件
            if sum(track)>target:
                return

            if sum(track)==target:
                res.append(track[:])
                return

            for i in range(len(nums)):
                if sum(track)+nums[i]>target:
                    break
                track.append(nums[i])
                backtrack(nums[i:],track)
                track.pop()

        candidates.sort()
        backtrack(candidates,[])

        return res





# class Solution:
#     def combinationSum(self, candidates, target):
#         res=[]
#
#         candidates.sort()
#         def backtrack(nums,track):
#
#             # 结束条件
#             if sum(track)>target:
#                 return
#
#             if sum(track)==target:
#                 # print(track)
#                 # print(res)
#                 res.append(track[:])
#                 # print(res)
#                 return
#
#             for i in range(len(nums)):
#                 # print(nums[i])
#                 # 排除不符合条件的
#                 if sum(track)+nums[i]>target:
#                     break
#
#                 track.append(nums[i])
#                 print('递归之前:',track)
#                 backtrack(nums[i:],track)
#                 track.pop()
#                 print('递归之后:',track)
#
#         backtrack(candidates, [])
#
#         return res

candidates=[8,7,4,3]
target=11

so=Solution()
res=so.combinationSum(candidates,target)

print(res)