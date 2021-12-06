"""
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for i in range(n)] for j in range(m)]
        dp[0] = [1 for i in dp[0]]
        for row in dp:
            row[0] = 1

        for row in range(1, m):
            for column in range(1, n):
                dp[row][column] = dp[row - 1][column] + dp[row][column - 1]

        return dp[-1][-1]


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    m = 3
    n = 7
    expected_result = 28
    assert solution.uniquePaths(m, n) == expected_result

    # Example 2:
    m = 3
    n = 2
    expected_result = 3
    # Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    # 1. Right -> Down -> Down
    # 2. Down -> Down -> Right
    # 3. Down -> Right -> Down
    assert solution.uniquePaths(m, n) == expected_result

    # Example 3:
    m = 7
    n = 3
    expected_result = 28
    assert solution.uniquePaths(m, n) == expected_result

    # Example 4:
    m = 3
    n = 3
    expected_result = 6
    assert solution.uniquePaths(m, n) == expected_result
