"""
https://leetcode.com/problems/regular-expression-matching/

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false
"""


class Solution(object):
    """
    Not my solution, leetcode's solution
    """
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    s = "aa"
    p = "a"
    # Output: false
    # Explanation: "a" does not match the entire string "aa".
    assert solution.isMatch(s, p) is False

    # Example 2:
    s = "aa"
    p = "a*"
    # Output: true
    # Explanation: '*' means zero or more of the preceding element, 'a'.Therefore, by repeating 'a' once, it becomes "aa".
    assert solution.isMatch(s, p) is True

    # Example 3:
    s = "ab"
    p = ".*"
    # Output: true
    # Explanation: ".*" means zero or more (*) of any character (.).
    assert solution.isMatch(s, p) is True

    # Example 4:
    s = "aab"
    p = "c*a*b"
    # Output: true
    # Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
    assert solution.isMatch(s, p) is True

    # Example 5:
    s = "mississippi"
    p = "mis*is*p*."
    # Output: false
    assert solution.isMatch(s, p) is False