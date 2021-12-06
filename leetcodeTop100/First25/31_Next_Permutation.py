"""
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:
Input: nums = [1]
Output: [1]
"""
from typing import List


class Solution:
    """
    Not my code, leetcode's
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            self.swap(nums, i, j)
        self.reverse(nums, i + 1)

    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [1, 2, 3]
    # Output: [1, 3, 2]
    solution.nextPermutation(nums)
    assert nums == [1, 3, 2]

    # Example 2:
    nums = [3, 2, 1]
    # Output: [1, 2, 3]
    solution.nextPermutation(nums)
    assert nums == [1, 2, 3]

    # Example 3:
    nums = [1, 1, 5]
    # Output: [1, 5, 1]
    solution.nextPermutation(nums)
    assert nums == [1, 5, 1]

    # Example 4:
    nums = [1]
    # Output: [1]
    solution.nextPermutation(nums)
    assert nums == [1]
