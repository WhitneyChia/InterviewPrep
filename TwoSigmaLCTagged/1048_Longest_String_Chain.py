"""
https://leetcode.com/problems/longest-string-chain/

You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere
in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is
a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
"""
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)
        dp = {}

        def max_cnts(word):
            if word in dp:
                return dp[word]
            if word not in words:
                return 0
            cnt = 1
            for i in range(len(word)):
                new = word[:i] + word[i + 1:]
                cnt = max(cnt, 1 + max_cnts(new))
            dp[word] = cnt
            return dp[word]

        ma = float('-inf')
        for w in words:
            ma = max(ma, max_cnts(w))

        return ma


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    expected_result = 4
    # Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
    assert solution.longestStrChain(words) == expected_result

    # Example 2:
    words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    expected_result = 5
    # Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
    assert solution.longestStrChain(words) == expected_result

    # Example 3:
    words = ["abcd", "dbqca"]
    expected_result = 1
    # Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
    # ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
    assert solution.longestStrChain(words) == expected_result
