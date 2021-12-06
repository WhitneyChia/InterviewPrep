"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

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

    def maxSubArray(self, nums: List[int]) -> int:
        sum1 = max_sum = nums[0]
        for i in nums[1:]:
            # we used [1:] because what if we are given with only one element that too a negative
            if sum1 < 0:
                sum1 = i
            else:
                sum1 = sum1 + i
            max_sum = max(max_sum, sum1)

        return max_sum