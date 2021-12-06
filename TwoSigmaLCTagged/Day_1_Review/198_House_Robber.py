"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        First did with a dp table, and then optimized space with only two variables
        Keep a running dp table that tracks the max you can rob by choosing between where you came from
        """

        # Simple case, can rob only one of the houses
        if len(nums) in {0, 1}:
            return nums[len(nums) - 1]

        # Initialize the first two max profits
        two_back_max = nums[0]
        one_back_max = max(nums[1], nums[0])
        max_profit = one_back_max

        # Iterate through the remaining houses and update variables
        for i in range(2, len(nums)):
            max_profit = max(two_back_max + nums[i], one_back_max)
            two_back_max = one_back_max
            one_back_max = max_profit

        # This should be the most you can rob
        return max_profit


if __name__ == "__main__":

    solution = Solution()
    test = [1, 2, 3, 1]
    assert solution.rob(test) == 4

    test = [2, 7, 9, 3, 1]
    assert solution.rob(test) == 12
