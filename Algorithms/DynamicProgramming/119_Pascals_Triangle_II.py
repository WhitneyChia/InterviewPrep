"""
https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        rows = [[1]]

        if rowIndex == 0:
            return rows[0]

        for i in range(1, rowIndex + 1):
            prevRight = rows[-1] + [0]
            prevLeft = [0] + rows[-1]
            curr = [a + b for a, b in zip(prevRight, prevLeft)]
            rows.append(curr)
        return rows[-1]
