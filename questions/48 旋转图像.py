# -*- coding: utf-8 -*-

'''
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

提示：

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
'''

[[1,2,3],
 [4,5,6],
 [7,8,9]]

#->

[[7,4,1],
 [8,5,2],
 [9,6,3]]

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n=len(matrix)

        matrix_new=[[0]*n for i in range(n)]

        # 逐列生成或者逐行生成
        for i in range(n):
            for j in range(n):
                matrix_new[j][n-1-i]=matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j]=matrix_new[i][j]


matrix=[[1,2,3],
 [4,5,6],
 [7,8,9]]

so=Solution()
so.rotate(matrix)

print(matrix)








