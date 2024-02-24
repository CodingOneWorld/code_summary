# -*- coding: utf-8 -*-

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：

输入：digits = ""
输出：[]

示例 3：

输入：digits = "2"
输出：["a","b","c"]



提示：

    0 <= digits.length <= 4
    digits[i] 是范围 ['2', '9'] 的一个数字。

https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/

https://leetcode.cn/problems/letter-combinations-of-a-phone-number/solutions/1291371/17-dian-hua-hao-ma-de-zi-mu-zu-he-di-gui-tcxk'''
from typing import List


class Solution:
    # 队列解法
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']

        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)

                for letter in phone[ord(digit) - 50]:
                    queue.append(tmp + letter)

        return queue

    # 回溯解法
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
               '9': 'wxyz'}  # 首先定义一个哈希表，把相应的数字和字母对应起来
        n = len(digits)  # 计算给定字符串中数字的长度
        if n == 0:
            return []

        def dfs(index):  # 定义递归回溯函数
            if index == n:  # 如果此时递归到了字符串中最后一个数字，则表示第一层深度搜索结束，将结果存储起来
                res.append(''.join(tmp))  # 注意一下这边存储的时候要把多个字符串组合成一个字符串，利用
                # join函数，这边还要注意的是后面会把tmp中的最上面字符弹出，这边利用join函数也同时避免
                # 了tmp弹出时影响res的目的，不然全部返回空字符串
            else:  # 如果这个时候没搜索到最后一层，则
                for i in dic[digits[index]]:  # 逐个遍历当前数字对应的字母
                    tmp.append(i)  # 将这个字母加到tmp中
                    dfs(index + 1)  # 因为要把下一个数字对应的字母继续加进去，所以这边index + 1，函数传递下一个位置
                    tmp.pop()  # 因为还需要把最后一个数字的字母逐个加进去，所以这边要把最后一个弹出，
                    # 因为上一行的dfs函数遇到结束条件，才回向下执行，所以这边已经完成一次深度的搜索，此时要把最后一个字母弹出，实现下一轮遍历

        res = []  # 初始化返回结果数组
        tmp = []  # 初始化过渡数组
        dfs(0)  # 首先执行index = 0，因为都是从第一个字母开始组合
        return res  # 返回结果函数


















class Solution:
    # 回溯 路径 选择 结束条件 选择列表
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
               '9': 'wxyz'}  # 首先定义一个哈希表，把相应的数字和字母对应起来
        n=len(digits)
        res=[]
        tmp=[]

        def backtrack(index):
            # 结束条件
            if index==n:
                res.append(''.join(tmp))
            # 选择列表
            else:
                for i in dic[digits[index]]:
                    tmp.append(i)
                    backtrack(index+1)
                    tmp.pop()

        backtrack(0)
        return res





