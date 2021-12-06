"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    """
    This is the sliding window approach, answer taken from LC
    """
    def lengthOfLongestSubstring(self, s):

        # This is the dictionary of where we've seen the char
        encountered = dict()

        # Start with index 0
        anchor = length = 0

        # Enumerate the string
        for i, c in enumerate(s):
            # if you've seen the char within your current window
            if c in encountered and encountered[c] >= anchor:
                # Move the anchor to the index after the first instance
                anchor = encountered[c] + 1
            else:
                # otherwise, check if this new length is greater than your old length
                length = max(length, i + 1 - anchor)
            # update the last place you've seen the char
            encountered[c] = i
        # the length should be the max length
        return length


if __name__ == "__main__":

    solution = Solution()
    s = "abcabcbb"
    # Explanation: The answer is "abc", with the length of 3.
    assert solution.lengthOfLongestSubstring(s) == 3

    s = "bbbbb"
    # Explanation: The answer is "b", with the length of 1.
    assert solution.lengthOfLongestSubstring(s) == 1

    s = "pwwkew"
    # Explanation: The answer is "wke", with the length of 3.
    assert solution.lengthOfLongestSubstring(s) == 3
