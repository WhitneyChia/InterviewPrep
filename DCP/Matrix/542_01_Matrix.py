"""
https://leetcode.com/problems/01-matrix/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
from typing import List


# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         m, n = len(matrix), len(matrix[0])
#         for i, row in enumerate(matrix):
#             for j, cell in enumerate(row):
#                 if cell:
#                     top = matrix[i-1][j] if i else float('inf')
#                     left = matrix[i][j-1] if j else float('inf')
#                     matrix[i][j] = min(top, left) + 1
#         for i in reversed(range(m)):
#             for j in reversed(range(n)):
#                 # This walrus operator is only available in python 3.8
#                 if cell := matrix[i][j]:
#                     bottom = matrix[i+1][j] if i < m - 1 else float('inf')
#                     right = matrix[i][j+1] if j < n - 1 else float('inf')
#                     matrix[i][j] = min(cell, bottom + 1, right + 1)
#         return matrix