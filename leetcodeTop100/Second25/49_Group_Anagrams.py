"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            if tuple(sorted(s)) in ans:
                ans[tuple(sorted(s))].append(s)
            else:
                ans[tuple(sorted(s))] = [s]
        return list(ans.values())


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_result = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert solution.groupAnagrams(strs) == expected_result

    # Example 2:
    strs = [""]
    expected_result = [[""]]
    assert solution.groupAnagrams(strs) == expected_result

    # Example 3:
    strs = ["a"]
    expected_result = [["a"]]
    assert solution.groupAnagrams(strs) == expected_result
