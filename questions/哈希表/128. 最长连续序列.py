# -*- coding: utf-8 -*-

'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9



提示：

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109

'''















# 寻找连续序列的开头，然后while循环看下一个数在不在数组中，进行count，更新最长的结果到res
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        nums=set(nums)
        # 遍历每个数 寻找可作为连续数列开头的数
        for num in nums:
            # 找到后，计算当前连续数列的长度，更新res
            if num-1 not in nums:
                seq_len=1
                while num+1 in nums:
                    seq_len+=1
                    num=num+1
                res=max(res,seq_len)

        return res

# 哈希表
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_dict=dict()
        max_length=0

        for num in nums:
            if num not in hash_dict:
                left=hash_dict.get(num-1,0)
                right=hash_dict.get(num+1,0)

                # 状态转换方程
                cur_length=1+left+right
                max_length=cur_length if cur_length>max_length else max_length
                # 数据存入hash表
                # 把头尾都设置为最长长度
                hash_dict[num]=cur_length
                hash_dict[num-left]=cur_length
                hash_dict[num+right]=cur_length
        return max_length


# 动态规划  做了排序 不满足时间复杂度为 O(n)
# 耗时60ms 击败99.92%使用 Python3 的用户
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(list(set(nums)))

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + 1 if nums[i] - nums[i - 1] == 1 else dp[i]

        return max(dp)















class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        max_length=0

        for num in nums:
            if num not in dic:
                left=dic.get(num-1,0)
                right=dic.get(num+1,0)

                cur_length=1+left+right

                # 更新最大长度
                max_length=max_length if max_length>cur_length else cur_length

                # 更新dic
                dic[num]=cur_length
                dic[num-1]=cur_length
                dic[num+1]=cur_length
        return max_length


