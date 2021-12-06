"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""
from typing import List


class Solution:
    """
    Not my solution, this was found in leetcode's comments and would be my approach, two binary searches
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def searchLow(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return right

        def searchHigh(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        start = searchLow(nums, target)
        end = searchHigh(nums, target)
        if 0 <= start < len(nums) and start <= end and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    # Output: [3, 4]
    assert solution.searchRange(nums, target) == [3, 4]

    # Example 2:
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    # Output: [-1, -1]
    assert solution.searchRange(nums, target) == [-1, -1]

    # Example 3:
    nums = []
    target = 0
    # Output: [-1, -1]
    assert solution.searchRange(nums, target) == [-1, -1]

    # My Example
    nums = [1, 1, 1, 1, 1, 1, 1]
    target = 1
    print(solution.searchRange(nums, target))

    # My Example
    nums = [100, 100, 100, 100, 100]
    target = 100
    print(solution.searchRange(nums, target))