"""
https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # The array's length should be 1 longer than the length of cost
        # This is because we can treat the "top floor" as a step to reach
        minimum_cost = [0] * (len(cost) + 1)

        # Start iteration from step 2, since the minimum cost of reaching
        # step 0 and step 1 is 0
        for i in range(2, len(cost) + 1):
            take_one_step = minimum_cost[i - 1] + cost[i - 1]
            take_two_steps = minimum_cost[i - 2] + cost[i - 2]
            minimum_cost[i] = min(take_one_step, take_two_steps)

        # The final element in minimum_cost refers to the top floor
        return minimum_cost[-1]


if __name__ == "__main__":

    solution = Solution()
    cost = [10, 15, 20]
    assert solution.minCostClimbingStairs(cost) == 15

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    assert solution.minCostClimbingStairs(cost) == 6


    def front_back(str):
        if len(str) == 0:
            return str
        list_str = list(str)
        list_str[0], list_str[len(str) - 1] = list_str[len(str) - 1], list_str[0]
        return "".join(list_str)

    test = ""
    print(front_back(test))
