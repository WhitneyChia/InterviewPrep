"""
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2
"""
from typing import List


class Solution:
    """
    Two pointers, moving inward. Track width and the lower of left or right is how to calculate volume at that point
    """
    def maxArea(self, height: List[int]) -> int:
        # initialize volume at zero
        volume = 0

        # Set the two pointers and initialize them as the max
        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]

        # Default width is the entire thing
        width = right - left

        # Move pointers inward
        while left < right:
            # Move left pointer in scenario
            if left_max <= right_max:
                volume = max(volume, width * left_max)
                left += 1
                left_max = max(left_max, height[left])
            # Move right pointer in scenario
            else:
                volume = max(volume, width * right_max)
                right -= 1
                right_max = max(right_max, height[right])
            width -= 1

        return volume


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # Output: 49
    # Explanation: Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
    # In this case, the max area of water (blue section) the container can contain is 49.
    assert solution.maxArea(height) == 49

    # Example 2:
    height = [1, 1]
    # Output: 1
    assert solution.maxArea(height) == 1

    # Example 3:
    height = [4, 3, 2, 1, 4]
    # Output: 16
    assert solution.maxArea(height) == 16

    # Example 4:
    height = [1, 2, 1]
    # Output: 2
    assert solution.maxArea(height) == 2
