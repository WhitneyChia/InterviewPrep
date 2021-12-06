"""
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an
array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: (x[0], x[1]))

        solution = [intervals[0]]

        for interval_index in range(1, len(intervals)):
            if solution[-1][1] >= intervals[interval_index][0]:
                solution[-1][1] = max(intervals[interval_index][1], solution[-1][1])
            else:
                solution.append(intervals[interval_index])

        return solution


if __name__ == "__main__":

    solution = Solution()
    test = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert solution.merge(test) == [[1, 6], [8, 10], [15, 18]]

    test = [[1, 4], [4, 5]]
    assert solution.merge(test) == [[1, 5]]
