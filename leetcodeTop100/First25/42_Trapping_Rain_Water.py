"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""
from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]
        volume = 0

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected_result = 6
    # Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
    # In this case, 6 units of rain water (blue section) are being trapped.
    assert solution.trap(height) == expected_result

    # Example 2:
    height = [4, 2, 0, 3, 2, 5]
    expected_result = 9
    assert solution.trap(height) == expected_result