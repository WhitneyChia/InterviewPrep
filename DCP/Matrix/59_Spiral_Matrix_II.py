"""
https://leetcode.com/problems/spiral-matrix-ii/

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
"""
from typing import List
import math


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0]*n for _ in range(n)]
        mid = math.ceil(n/2)
        loop = 0
        index = 1

        while loop < mid:
            num_times = n-1
            starti = startj = loop
            num_times -= 2*loop
            if num_times == 0:
                result[starti][startj] = index
                return result
            endj = endi = loop + num_times

            # Fill out the row from left to right
            for j in range(startj,endj):
                result[starti][j] = index
                index += 1

            # Fill out the column from top to bottom
            for i in range(starti,endi):
                result[i][endj] = index
                index += 1

            # Fill out the row from right to left
            for j in range(endj,startj,-1):
                result[endi][j] = index
                index += 1

            # Fill out the column from bottom to top
            for i in range(endi,starti,-1):
                result[i][startj] = index
                index += 1

            loop += 1
        return result


if __name__ == "__main__":

    solution = Solution()
    test = 3
    assert solution.generateMatrix(test) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
