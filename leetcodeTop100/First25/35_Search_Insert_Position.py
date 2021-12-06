"""
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [1, 3, 5, 6]
    target = 5
    # Output: 2
    assert solution.searchInsert(nums, target) == 2

    # Example 2:
    nums = [1, 3, 5, 6]
    target = 2
    # Output: 1
    assert solution.searchInsert(nums, target) == 1

    # Example 3:
    nums = [1, 3, 5, 6]
    target = 7
    # Output: 4
    assert solution.searchInsert(nums, target) == 4

    # Example 4:
    nums = [1, 3, 5, 6]
    target = 0
    # Output: 0
    assert solution.searchInsert(nums, target) == 0

    # Example 5:
    nums = [1]
    target = 0
    # Output: 0
    assert solution.searchInsert(nums, target) == 0


