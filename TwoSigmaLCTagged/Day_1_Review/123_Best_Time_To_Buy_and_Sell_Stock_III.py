"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple
transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:
Input: prices = [1]
Output: 0
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyFirstStock = prices[0]
        sellFirstStockProfit = 0

        buySecondStock = -prices[0]
        profitFromTwoTransactions = 0

        for currentPrice in prices:
            buyFirstStock = min(buyFirstStock, currentPrice)
            sellFirstStockProfit = max(sellFirstStockProfit, currentPrice - buyFirstStock)

            buySecondStock = max(buySecondStock, sellFirstStockProfit - currentPrice)
            profitFromTwoTransactions = max(profitFromTwoTransactions, buySecondStock + currentPrice)

        return profitFromTwoTransactions


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    expected_result = 6
    # Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    # Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
    assert solution.maxProfit(prices) == expected_result

    # Example 2:
    prices = [1, 2, 3, 4, 5]
    expected_result = 4
    # Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    # Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple
    # transactions at the same time. You must sell before buying again.
    assert solution.maxProfit(prices) == expected_result

    # Example 3:
    prices = [7, 6, 4, 3, 1]
    expected_result = 0
    # Explanation: In this case, no transaction is done, i.e.max profit = 0.
    assert solution.maxProfit(prices) == expected_result

    # Example 4:
    prices = [1]
    expected_result = 0
    assert solution.maxProfit(prices) == expected_result
