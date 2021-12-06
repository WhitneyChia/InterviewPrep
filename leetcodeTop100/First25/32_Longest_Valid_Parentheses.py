"""
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
"""


class Solution:
    """
    Not my solution, this is leetcode's solution 4 java translated to python
    This uses two pointers and O(N) with O(1) space
    Go from left right and then from right to left
    """
    def longestValidParentheses(self, s: str) -> int:
        left_count = right_count = max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                left_count += 1
            else:
                right_count += 1

            if left_count == right_count:
                max_length = max(max_length, 2 * right_count)
            elif right_count >= left_count:
                left_count = right_count = 0
        left_count = right_count = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left_count += 1
            else:
                right_count += 1

            if left_count == right_count:
                max_length = max(max_length, 2 * left_count)
            elif left_count >= right_count:
                left_count = right_count = 0
        return max_length


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    s = "(()"
    # Output: 2
    # Explanation: The longest valid parentheses substring is "()".
    assert solution.longestValidParentheses(s) == 2

    # Example 2:
    s = ")()())"
    # Output: 4
    # Explanation: The longest valid parentheses substring is "()()".
    assert solution.longestValidParentheses(s) == 4

    # Example 3:
    s = ""
    # Output: 0
    assert solution.longestValidParentheses(s) == 0
