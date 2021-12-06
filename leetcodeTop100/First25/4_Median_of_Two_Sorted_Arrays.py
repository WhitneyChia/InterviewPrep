"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000
"""
from typing import List


class Solution:
    """
    This is kind of like merge sort. We would use two pointers on the two arrays and keep adding to the new array.
    Then we can simply find the middle index or middle indices to calculate the median.
    THIS IS WRONG, THIS IS O(n + m), the question asks for O(log(m+n))
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        We make a new list to put our solution into
        This becomes O(N) space, we can probably do this O(1) by not making a new list
        since the given array space does not count against us.
        """
        merged_nums = []

        # Initialize our two pointers to start from the beginning
        i = 0
        j = 0

        # Merge the two arrays, once one is done, stop
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged_nums.append(nums1[i])
                i += 1
            else:
                merged_nums.append(nums2[j])
                j += 1

        # Because we stopped once one of the arrays was done, we may have leftovers to append to the solution
        # We can simply append because we were given that both arrays were sorted already
        if i < len(nums1):
            merged_nums += nums1[i:]
        if j < len(nums2):
            merged_nums += nums2[j:]

        # Median calculation, need to figure out if it is even or not, since that is a different calculation
        even = len(merged_nums) % 2 == 0

        # The two different ways of calculating the median
        if even:
            first_num = merged_nums[int(len(merged_nums) / 2 - 1)]
            second_num = merged_nums[int(len(merged_nums) / 2)]
            median = (first_num + second_num) / 2
        else:
            median = merged_nums[len(merged_nums) // 2]

        return median

    def findMedianSortedArraysLogRunTime(self, nums1: List[int], nums2: List[int]) -> float:
        """
        NeetCode explains this here: https://www.youtube.com/watch?v=q6IEA26hvXc
        It's partitioning left and rights in both lists
        """

        # First just make it so that A is always the smaller list
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1

        while True:
            i = (left + right) // 2  # A
            j = half - i - 2  # B

            a_left = A[i] if i >= 0 else float("-inf")
            a_right = A[i + 1] if (i + 1) < len(A) else float("inf")
            b_left = B[j] if j >= 0 else float("-inf")
            b_right = B[j + 1] if (j + 1) < len(B) else float("inf")

            # partition is correct
            if a_left <= b_right and b_left <= a_right:
                # odd
                if total % 2:
                    return min(a_right, b_right)
                # even
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    # Output: 2.00000
    # Explanation: merged array = [1, 2, 3] and median is 2.
    assert solution.findMedianSortedArrays(nums1, nums2) == 2

    # Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    # Output: 2.50000
    # Explanation: merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.5

    # Example 3:
    nums1 = [0, 0]
    nums2 = [0, 0]
    # Output: 0.00000
    assert solution.findMedianSortedArrays(nums1, nums2) == 0

    # Example 4:
    nums1 = []
    nums2 = [1]
    # Output: 1.00000
    assert solution.findMedianSortedArrays(nums1, nums2) == 1

    # Example 5:
    nums1 = [2]
    nums2 = []
    # Output: 2.00000
    assert solution.findMedianSortedArrays(nums1, nums2) == 2

    # Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    # Output: 2.00000
    # Explanation: merged array = [1, 2, 3] and median is 2.
    assert solution.findMedianSortedArraysLogRunTime(nums1, nums2) == 2

    # Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    # Output: 2.50000
    # Explanation: merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.
    assert solution.findMedianSortedArraysLogRunTime(nums1, nums2) == 2.5

    # Example 3:
    nums1 = [0, 0]
    nums2 = [0, 0]
    # Output: 0.00000
    assert solution.findMedianSortedArraysLogRunTime(nums1, nums2) == 0

    # Example 4:
    nums1 = []
    nums2 = [1]
    # Output: 1.00000
    assert solution.findMedianSortedArraysLogRunTime(nums1, nums2) == 1

    # Example 5:
    nums1 = [2]
    nums2 = []
    # Output: 2.00000
    assert solution.findMedianSortedArraysLogRunTime(nums1, nums2) == 2
