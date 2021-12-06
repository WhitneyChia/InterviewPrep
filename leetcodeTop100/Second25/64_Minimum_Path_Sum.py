"""
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""


class Solution:
    def minPathSum(self, grid):
        r, c = len(grid), len(grid[0])
        for i in range(1, r):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1, c):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    expected_result = 7
    # Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
    assert solution.minPathSum(grid) == expected_result

    # Example 2:
    grid = [[1, 2, 3], [4, 5, 6]]
    expected_result = 12
    assert solution.minPathSum(grid) == expected_result
