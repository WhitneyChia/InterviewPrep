"""
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Because this is in a cycle, this degenerates to two regular house robber calls
        One from 0 to n - 1 and one from 1 to n.
        We can take the solution from House Robber and just call it twice on the two options
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        first_cycle_nums = nums[:- 1]
        first_cycle = self.regular_rob_house(first_cycle_nums)
        second_cycle_nums = nums[1:]
        second_cycle = self.regular_rob_house(second_cycle_nums)
        return max(first_cycle, second_cycle)

    def regular_rob_house(self, nums):
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

    # Example 1:
    nums = [2, 3, 2]
    expected_result = 3
    assert solution.rob(nums) == expected_result

    # Example 2:
    nums = [1, 2, 3, 1]
    expected_result = 4
    assert solution.rob(nums) == expected_result

    # Example 3:
    nums = [1, 2, 3]
    expected_result = 3
    assert solution.rob(nums) == expected_result

    # My Test
    nums = [200, 3, 140, 20, 10]
    expected_result = 340
    assert solution.rob(nums) == expected_result
