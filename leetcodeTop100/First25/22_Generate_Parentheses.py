"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""
from typing import List


class Solution:
    """
    not my solution, this is leetcode's, this is backtracking
    """
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans


if __name__ == "__main__":

    solution = Solution()
    # Example 1:
    n = 3
    # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert solution.generateParenthesis(n) == ["((()))", "(()())", "(())()", "()(())", "()()()"]

    # Example 2:
    Input: n = 1
    # Output: ["()"]
    assert solution.generateParenthesis(n) == ["()"]

