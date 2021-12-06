"""
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""


class Solution:
    """ The search space becomes 0 to x + 1"""

    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        return left - 1


if __name__ == "__main__":

    solution = Solution()
    print(solution.mySqrt(4))

    print("\n")
    print(solution.mySqrt(8))

    print("\n")
    print(solution.mySqrt(10))