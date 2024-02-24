# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    # def numberOfPairs(self, nums):
    #     tag=[1 for i in range(len(nums))]
    #     count=0
    #     for i in range(len(nums)-1):
    #         for j in range(i+1,len(nums)):
    #             print(i)
    #             print(j)
    #             if nums[i]==nums[j] and tag[j]==1 and tag[i]==1:
    #                 count+=1
    #                 # nums=nums[i+1:j]+nums[j+1:len(nums)-1]
    #                 tag[i]=0
    #                 tag[j]=0
    #                 print(tag)
    #                 break
    #     return [count,sum(tag)]

    def numberOfPairs(self, nums):

        for c in Counter(nums).values():
            print(c)
        # print(Counter(nums).values())
        pairs = sum(c // 2 for c in Counter(nums).values())
        return [pairs, len(nums) - pairs * 2]


if __name__ == '__main__':
    nums=[1,1]
    nums=[1,3,2,1,3,2,2]
    solution=Solution()
    res=solution.numberOfPairs(nums)
    print(res)

    # tag = [i for i in range(len(nums))]
    # print(tag)