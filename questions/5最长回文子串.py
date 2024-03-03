# -*- coding: utf-8 -*-

"""
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：

输入：s = "cbbd"
输出："bb"



提示：

    1 <= s.length <= 1000
    s 仅由数字和英文字母组成


"""
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n=len(s)
        res=''

        for i in range(n):
            # 奇数
            l=i-1
            r=i+1
            while l>0 and r<n and s[l]==s[r]:
                l=i-1
                r=r+1
            if r-l-1>len(res):
                res=s[l+1:r]

            # 偶数
            l=i
            r=i+1
            while l>0 and r<n and s[l]==s[r]:
                l=i-1
                r=r+1
            if r-l-1>len(res):
                res=s[l+1:r]

        return res







class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''

        for i in range(n):
            # 回文子串奇数，起始位置
            l = i - 1
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l = l - 1
                r = r + 1

            if r - l - 1 > len(res):
                res = s[l + 1:r]

            # 回文子串为偶数，起始位置
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l = l - 1
                r = r + 1

            if r - l - 1 > len(res):
                res = s[l + 1:r]

        return res
