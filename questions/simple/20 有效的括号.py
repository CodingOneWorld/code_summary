# -*- coding: utf-8 -*-

'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    每个右括号都有一个对应的相同类型的左括号。



示例 1：

输入：s = "()"
输出：true

示例 2：

输入：s = "()[]{}"
输出：true

示例 3：

输入：s = "(]"
输出：false



提示：

    1 <= s.length <= 104
    s 仅由括号 '()[]{}' 组成


'''
class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','[':']','{':'}','?':'?'}
        stack=['?']
        for char in s:
            if char in dic:
                stack.append(char)
            elif dic[stack.pop()]!=char:
                return False
        return len(stack)==1













# 标准答案
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1

s = "()[]{}"
so=Solution()
res=so.isValid(s)
print(res)
