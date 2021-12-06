"""
https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index, and each
element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= right:
                right = i

        return right == 0


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [2, 3, 1, 1, 4]
    # expected_result = True
    # Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    assert solution.canJump(nums)

    # Example 2:
    nums = [3, 2, 1, 0, 4]
    # expected_result = False
    # Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
    # which makes it impossible to reach the last index.
    assert not solution.canJump(nums)
