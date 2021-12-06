"""
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums = [1, 2, 3]
    expected_result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1],  [3, 2, 1], [3, 1, 2]]
    assert solution.permute(nums) == expected_result

    # Example 2:
    nums = [0, 1]
    expected_result = [[0, 1], [1, 0]]
    assert solution.permute(nums) == expected_result

    # Example 3:
    nums = [1]
    expected_result = [[1]]
    assert solution.permute(nums) == expected_result
