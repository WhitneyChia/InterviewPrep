"""
Given an array nums which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9

Example 3:
Input: nums = [1,4,4], m = 3
Output: 4
"""

from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def feasible(threshold) -> bool:
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > m:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":

    solution = Solution()
    nums = [7, 2, 5, 10, 8]
    m = 2

    print(solution.splitArray(nums, m))

    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    m = 2

    print(solution.splitArray(nums, m))