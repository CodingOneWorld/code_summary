# -*- coding: utf-8 -*-

'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

https://blog.csdn.net/2503_91125378/article/details/146313736

'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_v = 0
        len_l = len(height)
        i = 0
        j = len_l - 1

        while i < j:
            l = j - i
            w = min([height[i], height[j]])
            if l * w >= max_v:
                max_v = l * w

            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1

        return max_v




height=[1,2,4,3]
s=Solution()
print(s.maxArea(height))