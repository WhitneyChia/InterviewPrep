"""
https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end_iterations = len(nums) - 1
        i = 0

        while i <= end_iterations:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                end_iterations -= 1
            else:
                i += 1


if __name__ == "__main__":

    solution = Solution()
    test = [0, 1, 0, 3, 12]
    solution.moveZeroes(test)
    assert test == [1, 3, 12, 0, 0]
