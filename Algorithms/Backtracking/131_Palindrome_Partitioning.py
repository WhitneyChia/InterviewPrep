"""
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # dp[i][j] == 1 means that s[i:j+1] is a palindrome
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        # Traverse dp in diagonals middle to topright corner
        # j is starting character and j+i is ending character
        for i in range(len(s)):
            for j in range(len(s) - i):

                if s[j] == s[j + i]:
                    # endpoint match with len 1 or 2 equals automatic palindrome
                    if i <= 1:
                        dp[j][j + i] = 1
                    # endpoint match with inner palindrome equals palindrome
                    elif dp[j + 1][j + i - 1]:
                        dp[j][j + i] = 1

        result = []
        # dps build out the answer arrays
        self.builder(0, s, [], dp, result)
        return result

    def builder(self, ptr, s, building, dp, result):

        # traverse all palindromes in a given row
        for i in range(ptr, len(s)):
            # if we find a palindrome
            if dp[ptr][i]:
                # extend the array we are building
                newBuild = building.copy()
                newBuild.append(s[ptr:i + 1])
                # when we reach the end of the string append to result
                if i == len(s) - 1:
                    result.append(newBuild)
                # otherwise move pointer up and recurse
                else:
                    self.builder(i + 1, s, newBuild, dp, result)


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    s = "aab"
    expected_result = [["a", "a", "b"], ["aa", "b"]]
    assert solution.partition(s) == expected_result

    # Example 2:
    s = "a"
    expected_result = [["a"]]
    assert solution.partition(s) == expected_result
