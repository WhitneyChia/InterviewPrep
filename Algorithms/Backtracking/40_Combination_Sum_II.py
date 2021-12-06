"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a
target number (target), find all unique combinations in candidates where
the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
"""
from typing import List
from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                # make a deep copy of the current combination
                #   rather than keeping the reference.
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]

                if freq <= 0:
                    continue

                # add a new element to the current combination
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)

                # continue the exploration with the updated combination
                backtrack(comb, remain - candidate, next_curr, counter, results)

                # backtrack the changes, so that we can try another candidate
                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []  # container to hold the final combinations
        counter = Counter(candidates)
        # convert the counter table to a list of (num, count) tuples
        counter = [(c, counter[c]) for c in counter]

        backtrack(comb = [], remain = target, curr = 0,
                  counter = counter, results = results)

        return results


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    expected_result = [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ]
    assert solution.combinationSum2(candidates, target) == expected_result

    # Example 2:
    candidates = [2, 5, 2, 1, 2]
    target = 5
    expected_result = [
        [2, 2, 1],
        [5]
    ]
    assert solution.combinationSum2(candidates, target) == expected_result