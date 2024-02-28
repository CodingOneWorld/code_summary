# -*- coding: utf-8 -*-

'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：

输入：height = [4,2,0,3,2,5]
输出：9

'''
from _ast import List



# 暴力解法
# 搜索每个位置左边，右边最高的位置，计算该位置能存储水的面积
class Solution:
    def trap(self, height):

        left=0
        right=0
        S=0

        if len(height)<=2:
            return 0

        if len(set(height)) <= 1:
            return 0

        for i in range(1,len(height)-1):
            print(i)
            left=max(height[0:i])
            right=max(height[i+1:])

            target=min(left,right)
            s=target-height[i] if target>height[i] else 0
            S+=s

        return S


# 动态规划
# 先遍历得到每个下标的左边最大值，右边最大值
# 再遍历计算每个下标处能接的雨水
class Solution:
    def trap(self, height):

        if len(height)<=2:
            return 0

        if len(set(height))<=1:
            return 0

        left_max=[0]*len(height)
        right_max=[0]*len(height)

        left_max[0]=height[0]
        right_max[-1]=height[-1]

        for i in range(1,len(height)):
            l_max=max(left_max[i-1],height[i])
            left_max[i]=l_max

        for i in range(len(height)-2,-1,-1):
            r_max=max(right_max[i+1],height[i])
            right_max[i] = r_max

        for i in range(len(height)):
            s=min(left_max[i],right_max[i])-height[i]


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans





height = [4,2,0,3,2,5]
so=Solution()
res=so.trap(height)
print(res)

