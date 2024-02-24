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


