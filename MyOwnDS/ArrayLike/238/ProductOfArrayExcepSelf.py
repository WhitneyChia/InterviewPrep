"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
from functools import reduce
from typing import List

# This uses division except during ZeroDivisionError
# TODO do this correctly without division -> two arrays, left to right and right to left products
# Kind of have it already with the ZeroDivisionError code


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_product = self.reduce_list_to_product(nums)

        res = []
        for i in range(len(nums)):
            try:
                res.append(int(total_product / nums[i]))
            except ZeroDivisionError:
                left_side = self.reduce_list_to_product(nums[0:i])
                right_side = self.reduce_list_to_product(nums[i + 1:len(nums)])
                res.append(int(left_side * right_side))
        return res

    def reduce_list_to_product(self, nums):
        if nums:
            total_product = reduce(lambda x, y: x * y, nums)
            return total_product
        return 1