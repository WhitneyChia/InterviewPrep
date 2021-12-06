"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any
time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""
from typing import List


class Solution:
    """
    Surprisingly simple, basically just keep incrementing positive scenarios vs. idx - 1.
    Ignore if going neg
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx - 1]:
                max_profit += prices[idx] - prices[idx - 1]

        return max_profit


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    prices = [7, 1, 5, 3, 6, 4]
    expected_result = 7
    # Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    # Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    # Total profit is 4 + 3 = 7.
    assert solution.maxProfit(prices) == expected_result

    # Example 2:
    prices = [1, 2, 3, 4, 5]
    expected_result = 4
    # Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    assert solution.maxProfit(prices) == expected_result

    # Example 3:
    prices = [7, 6, 4, 3, 1]
    expected_result = 0
    # Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum
    # profit of 0.
    assert solution.maxProfit(prices) == expected_result
