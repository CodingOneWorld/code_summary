# -*- coding: utf-8 -*-

'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。



示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3



提示：

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] 的值为 '0' 或 '1'


'''



















# 递归
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        result = 0
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    result += 1
                    self._numIslands(grid, row, col)
        return result

    def _numIslands(self, grid, x, y):
        grid[x][y] = '0'
        if 0 < x and grid[x - 1][y] == '1':
            self._numIslands(grid, x - 1, y)

        if 0 < y and grid[x][y - 1] == '1':
            self._numIslands(grid, x, y - 1)

        if y < len(grid[0]) - 1 and grid[x][y + 1] == '1':
            self._numIslands(grid, x, y + 1)

        if x < len(grid) - 1 and grid[x + 1][y] == '1':
            self._numIslands(grid, x + 1, y)


# 广度优先搜索
class Solution(object):

    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > '0':
                    counter += 1
                    self.dfs(grid, i, j)

        return counter

    def dfs(self, grid, i, j):

        # 如果越界或到达边线
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return

            # 对遍历过的点一律设为 0
        grid[i][j] = '0'
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)


# 广度优先算法  非类函数写法
class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(i, j, grid):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return

            grid[i][j] = '0'

            dfs(i - 1, j, grid)
            dfs(i + 1, j, grid)
            dfs(i, j - 1, grid)
            dfs(i, j + 1, grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j, grid)

        return count