"""
https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        logic is:
        a ^ 0 -> a
        a ^ a -> 0
        a ^ b ^ a -> a ^ a ^ b -> 0 ^ b -> b
        """

        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]

        return ans


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [2, 2, 1]
    expected_result = 1
    assert solution.singleNumber(nums) == expected_result

    # Example 2:
    nums = [4, 1, 2, 1, 2]
    expected_result = 4
    assert solution.singleNumber(nums) == expected_result

    # Example 3:
    nums = [1]
    expected_result = 1
    assert solution.singleNumber(nums) == expected_result
