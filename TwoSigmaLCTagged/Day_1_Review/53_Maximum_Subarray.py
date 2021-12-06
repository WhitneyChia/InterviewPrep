"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""
from typing import List


class Solution:
    """ This is Kadane's algorithm """
    def maxSubArray(self, nums: List[int]) -> int:
        ans = cur = nums[0]
        for x in nums[1:]:
            cur = x + max(cur, 0)
            ans = max(ans, cur)
        return ans


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected_result = 6
    # Explanation: [4, -1, 2, 1] has the largest sum = 6.
    assert solution.maxSubArray(nums) == expected_result

    # Example 2:
    nums = [1]
    expected_result = 1
    assert solution.maxSubArray(nums) == expected_result

    # Example 3:
    nums = [5, 4, -1, 7, 8]
    expected_result = 23
    assert solution.maxSubArray(nums) == expected_result
