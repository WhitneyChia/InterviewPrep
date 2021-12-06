"""
https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates,
return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def backtracking(nums, start, end, curr, result):

            result.append(list(curr))

            for i in range(start, end):

                if i == start or (i > start and nums[i] != nums[i - 1]):
                    curr.append(nums[i])
                    backtracking(nums, i + 1, end, curr, result)
                    curr.remove(nums[i])

        backtracking(nums, 0, len(nums), [], result)
        return result


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [1, 2, 2]
    expected_result = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert solution.subsetsWithDup(nums) == expected_result

    # Example 2:
    nums = [0]
    expected_result = [[], [0]]
    assert solution.subsetsWithDup(nums) == expected_result

