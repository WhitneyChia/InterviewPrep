"""
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of
the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        backtrack()
        return output


if __name__ == "__main__":

    solution = Solution()
    # Example 1:
    n = 4
    k = 2
    expected_result = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4]
    ]
    assert solution.combine(n, k) == expected_result

    # Example 2:
    n = 1
    k = 1
    expected_result = [[1]]
    assert solution.combine(n, k) == expected_result
