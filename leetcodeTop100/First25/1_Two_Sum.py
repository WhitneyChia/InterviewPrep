"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        O(N) time and O(N) space because of seen
        My own solution
        """

        # Track the numbers we've seen so far, number and the index since we have to return the index, O(N) space
        seen = {}

        for i in range(len(nums)):
            # Calculate the complement
            complement = target - nums[i]

            # If it is seen, return i and the index of the complement
            if complement in seen:
                # short circuit and just return, but worst case is still O(N)
                return [seen[complement], i]
            # Otherwise enter in the number in seen
            else:
                seen[nums[i]] = i


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    assert solution.twoSum(nums, target) == [0, 1]

    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2]

    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [0, 1]

