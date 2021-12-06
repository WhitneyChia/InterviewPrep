"""
https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the
combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.

Example 5:
Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    k = 3
    n = 7
    expected_result = [[1, 2, 4]]
    # Explanation: 1 + 2 + 4 = 7 There are no other valid combinations.
    assert solution.combinationSum3(k, n) == expected_result

    # Example 2:
    k = 3
    n = 9
    expected_result = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    # Explanation: 1 + 2 + 6 = 9 1 + 3 + 5 = 9 2 + 3 + 4 = 9
    # There are no other valid combinations.
    assert solution.combinationSum3(k, n) == expected_result

    # Example 3:
    k = 4
    n = 1
    expected_result =  []
    # Explanation: There are no valid combinations.
    # Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10
    # and since 10 > 1, there are no valid combination.
    assert solution.combinationSum3(k, n) == expected_result

    # Example 4:
    k = 3
    n = 2
    expected_result = []
    # Explanation: There are no valid combinations.
    assert solution.combinationSum3(k, n) == expected_result

    # Example 5:
    k = 9
    n = 45
    expected_result = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    # Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45 There are no other valid combinations.
    assert solution.combinationSum3(k, n) == expected_result