"""
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [1, 2, 3]
    # Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    res = solution.subsets(nums)
    assert res == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

    # Example 2:
    nums = [0]
    # Output: [[], [0]]
    assert solution.subsets(nums) == [[], [0]]
