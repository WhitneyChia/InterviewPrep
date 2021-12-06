"""
https://leetcode.com/problems/maximum-sum-circular-subarray/

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array. Formally, the next element
of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i],
nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:
Input: nums = [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:
Input: nums = [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:
Input: nums = [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
"""
from typing import List
import math


class Solution:
    def maxSubarray(self, nums):
        """ This is Kadane's """
        _max = prev = nums[0]

        for i in range(1, len(nums)):
            prev = max(nums[i], nums[i] + prev)
            _max = max(_max, prev)

        return _max

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_non_circular_arr = self.maxSubarray(nums)

        _sum = 0
        for idx in range(len(nums)):
            _sum += nums[idx]
            nums[idx] *= -1

        max_non_circular_inverted_arr = self.maxSubarray(nums)

        """
        if max_circular == 0 => sum == inverted_circular * -1 it is posible when all nums less than 0 or more than 0 => 
        max == max_non_circular (large negative num or sum of all nums (all nums is positive))
        """
        max_circular_arr = _sum - max_non_circular_inverted_arr * -1

        return max(max_non_circular_arr, max_circular_arr) if max_circular_arr != 0 else max_non_circular_arr
