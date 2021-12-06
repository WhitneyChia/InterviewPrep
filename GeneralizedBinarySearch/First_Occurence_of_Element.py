"""
Given a sorted array, return the earliest occurrence of an integer.
If not present, return -1

Example 1:
Input: nums = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401] target = 108
Output: 3
"""
from typing import List


class Solution:

    def search_first_of_k(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = -1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                right = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return result


if __name__ == "__main__":

    solution = Solution()
    nums = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 108

    print(solution.search_first_of_k(nums, target))