"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n in {0, 1}:
            return 1

        two_behind = 1
        one_behind = 1
        solution = 2

        for i in range(0, n - 1):
            solution = one_behind + two_behind
            two_behind = one_behind
            one_behind = solution

        return solution


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    n = 2
    expected_result = 2
    # Explanation: There are two ways to climb to the top.
    # 1. 1 step + 1 step
    # 2. 2 steps
    assert solution.climbStairs(n) == expected_result

    # Example 2:
    n = 3
    expected_result = 3
    # Explanation: There are three ways to climb to the top.
    # 1. 1 step + 1 step + 1 step
    # 2. 1 step + 2 steps
    # 3. 2 steps + 1 step
    assert solution.climbStairs(n) == expected_result
