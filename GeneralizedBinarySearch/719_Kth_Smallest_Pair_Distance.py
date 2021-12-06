"""
https://leetcode.com/problems/find-k-th-smallest-pair-distance/

The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the
pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:
Input: nums = [1,3,1], k = 1
Output: 0

Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:
Input: nums = [1,1,1], k = 2
Output: 0

Example 3:
Input: nums = [1,6,1], k = 3
Output: 5
"""
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def enough(distance) -> bool:  # two pointers
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:  # fast pointer
                    j += 1
                count += j - i - 1  # count pairs
                i += 1  # move slow pointer
            return count >= k

        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [1, 3, 1]
    k = 1
    expected_result = 0
    # Explanation: Here are all the pairs:
    # (1,3) -> 2
    # (1,1) -> 0
    # (3,1) -> 2
    # Then the 1st smallest distance pair is (1,1), and its distance is 0.
    assert solution.smallestDistancePair(nums, k) == expected_result

    # Example 2:
    nums = [1, 1, 1]
    k = 2
    expected_result = 0
    assert solution.smallestDistancePair(nums, k) == expected_result

    # Example 3:
    nums = [1, 6, 1]
    k = 3
    expected_result = 5
    assert solution.smallestDistancePair(nums, k) == expected_result
