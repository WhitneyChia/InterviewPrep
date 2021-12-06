"""
https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input: s = "acdcb", p = "a*c?b"
Output: false
"""


class Solution:
    """ This is with backtracking """
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            # If the pattern caracter = string character
            # or pattern character = '?'
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1

            # If pattern character = '*'
            elif p_idx < p_len and p[p_idx] == '*':
                # Check the situation
                # when '*' matches no characters
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1

            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern
            elif star_idx == -1:
                return False

            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx

        # The remaining characters in the pattern should all be '*' characters
        return all(p[i] == '*' for i in range(p_idx, p_len))


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    s = "aa"
    p = "a"
    expected_result = False
    # Explanation: "a" does not match the entire string "aa".
    assert solution.isMatch(s, p) == expected_result

    # Example 2:
    s = "aa"
    p = "*"
    expected_result = True
    # Explanation: '*' matches any sequence.
    assert solution.isMatch(s, p) == expected_result

    # Example 3:
    s = "cb"
    p = "?a"
    expected_result = False
    # Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
    assert solution.isMatch(s, p) == expected_result

    # Example 4:
    s = "adceb"
    p = "*a*b"
    expected_result = True
    # Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
    assert solution.isMatch(s, p) == expected_result

    # Example 5:
    s = "acdcb"
    p = "a*c?b"
    expected_result = False
    assert solution.isMatch(s, p) == expected_result
