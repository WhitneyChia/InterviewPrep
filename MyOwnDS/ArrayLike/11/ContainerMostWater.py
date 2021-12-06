"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
 are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
 the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        left_max = height[left_pointer]
        right_max = height[right_pointer]
        width = right_pointer - left_pointer

        while left_pointer < right_pointer:
            if left_max <= right_max:
                volume = max(left_max * width, volume)
                left_pointer += 1
                left_max = max(left_max, height[left_pointer])
                width -= 1
            else:
                volume = max(right_max * width, volume)
                right_pointer -= 1
                right_max = max(right_max, height[right_pointer])
                width -= 1
        return volume