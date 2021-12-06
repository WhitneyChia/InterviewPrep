"""
https://leetcode.com/problems/unique-binary-search-trees/

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n
nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
"""


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    n = 3
    expected_result = 5
    assert solution.numTrees(n) == expected_result

    # Example 2:
    n = 1
    expected_result = 1
    assert solution.numTrees(n) == expected_result
