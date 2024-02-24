# -*- coding: utf-8 -*-

'''
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的所有字母得到的一个新单词。



示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:

输入: strs = [""]
输出: [[""]]

示例 3:

输入: strs = ["a"]
输出: [["a"]]



提示：

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] 仅包含小写字母

'''
from _ast import List


class Solution:
    def groupAnagrams(self, strs):
        set_str=set([])
        for s in strs:
            set_str.add(''.join(sorted(s)))

        # 建立字典
        dic={}
        i=0
        for s in set_str:
            dic[s]=i
            i+=1

        res=[[] for i in range(len(dic.keys()))]
        for s in strs:
            s2=''.join(sorted(s))
            res[dic[s2]].append(s)

        return res


class Solution:
    def groupAnagrams(self, strs):
        set_strs=set()
        for s in strs:
            set_strs.add(''.join(sorted(s)))

        dic = {}
        for str in set_strs:
            dic[str]=[]

        # 构建字典
        for s in strs:
            key=''.join(sorted(s))
            print(key)
            dic[key].append(s)
        return list(dic.values())


strs=["eat", "tea", "tan", "ate", "nat", "bat"]
# strs=[""]
# strs=["a"]
so=Solution()
res=so.groupAnagrams(strs)
print(res)

