"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
"""


class Solution:
    """
    Not my solution, taken from leetcode, jason0713 user
    """

    def longestPalindrome(self, s: str) -> str:
        self.maxlen = 0
        self.start = 0

        # Iterate through the string, treating every char as the center and check
        # Two scenarios for center, odd length is one letter, even length is two letters
        for i in range(len(s)):
            self.expandFromCenter(s, i, i)
            self.expandFromCenter(s, i, i + 1)
        return s[self.start:self.start + self.maxlen]

    def expandFromCenter(self, s, l, r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        if self.maxlen < r - l - 1:
            self.maxlen = r - l - 1
            self.start = l + 1


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    s = "babad"
    # Output: "bab"
    # Note: "aba" is also a valid answer.
    assert solution.longestPalindrome(s) == "bab"

    # Example 2:
    s = "cbbd"
    # Output: "bb"
    assert solution.longestPalindrome(s) == "bb"

    # Example 3:
    s = "a"
    # Output: "a"
    assert solution.longestPalindrome(s) == "a"

    # Example 4:
    s = "ac"
    # Output: "a"
    assert solution.longestPalindrome(s) == "a"
