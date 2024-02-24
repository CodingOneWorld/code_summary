# -*- coding: utf-8 -*-

'''
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

    例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。

请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。



示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。



提示：

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    prerequisites[i] 中的所有课程对 互不相同

https://leetcode.cn/circle/discuss/8jb70r/
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        clen = len(prerequisites)
        if clen == 0:
            return True

        # 步骤1：统计每个顶点的入度
        # 入度数组，记录了指向它的结点的个数，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表，使用散列表是为了去重
        adj = [set() for _ in range(numCourses)]

        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # [0, 1] 表示 1 在先，0 在后
        # 注意：邻接表存放的是后继 successor 结点的集合
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        # 步骤2：拓扑排序开始之前，先把所有入度为 0 的结点加入到一个队列中
        # 首先遍历一遍，把所有入度为 0 的结点都加入队列
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        counter = 0
        while queue:
            top = queue.pop(0)
            counter += 1
            # 步骤3：把这个结点的所有后继结点的入度减去 1，如果发现入度为 0 ，就马上添加到队列中
            for successor in adj[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)

        return counter == numCourses
