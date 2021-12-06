"""
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at
most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it
so that there is still at least one element left and the sum of the remaining elements is maximum possible.
Note that the subarray needs to be non-empty after deleting one element.

Example 1:
Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.

Example 2:
Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.

Example 3:
Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
"""
from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # noDeletions, oneDeletion, max
        nodel_sum = mx = arr[0]
        onedel_sum = max(arr[0], 0)

        for i in range(1, len(arr)):
            onedel_sum = max(arr[i], arr[i] + onedel_sum, max(0, arr[i]) + nodel_sum)
            # This is straightforward Kadane's on the no deletions
            nodel_sum = max(arr[i], arr[i] + nodel_sum)
            mx = max(mx, nodel_sum, onedel_sum)

        return mx

