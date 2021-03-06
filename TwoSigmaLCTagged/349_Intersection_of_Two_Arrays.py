"""
https://leetcode.com/problems/intersection-of-two-arrays/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result
must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""


class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    expected_result = [2]
    assert solution.intersection(nums1, nums2) == expected_result

    # Example 2:
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    expected_result = [9, 4]
    # Explanation: [4, 9] is also accepted.
    assert solution.intersection(nums1, nums2) == expected_result
