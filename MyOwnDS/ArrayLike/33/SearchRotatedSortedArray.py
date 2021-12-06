"""
In a rotated sorted array, return the index of a target number, -1 if not found
"""

from typing import List

# class Solution:
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         def find_rotate_index(left, right):
#             if nums[left] < nums[right]:
#                 return 0
#
#             while left <= right:
#                 pivot = (left + right) // 2
#                 if nums[pivot] > nums[pivot + 1]:
#                     return pivot + 1
#                 else:
#                     if nums[pivot] < nums[left]:
#                         right = pivot - 1
#                     else:
#                         left = pivot + 1
#
#         def search(left, right):
#             """
#             Binary search
#             """
#             while left <= right:
#                 pivot = (left + right) // 2
#                 if nums[pivot] == target:
#                     return pivot
#                 else:
#                     if target < nums[pivot]:
#                         right = pivot - 1
#                     else:
#                         left = pivot + 1
#             return -1
#
#         n = len(nums)
#
#         if n == 1:
#             return 0 if nums[0] == target else -1
#
#         rotate_index = find_rotate_index(0, n - 1)
#
#         # if target is the smallest element
#         if nums[rotate_index] == target:
#             return rotate_index
#         # if array is not rotated, search in the entire array
#         if rotate_index == 0:
#             return search(0, n - 1)
#         if target < nums[0]:
#             # search on the right side
#             return search(rotate_index, n - 1)
#         # search on the left side
#         return search(0, rotate_index)


class SimplerSolution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1