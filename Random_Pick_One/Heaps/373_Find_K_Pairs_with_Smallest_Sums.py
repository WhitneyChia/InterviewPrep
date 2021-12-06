"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""
from typing import List
from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # store pair as (sum, index_nums1, index_nums2)
        minHeap = [(nums1[0] + nums2[0], 0, 0)]
        seen = set()
        res = []

        while minHeap and len(res) != k:
            s, i, j = heappop(minHeap)
            res.append([nums1[i], nums2[j]])

            cand1 = (nums1[i + 1] + nums2[j], i + 1, j) if i + 1 < len(nums1) else None
            cand2 = (nums1[i] + nums2[j + 1], i, j + 1) if j + 1 < len(nums2) else None

            if cand1 and cand1 not in seen:
                seen.add(cand1)
                heappush(minHeap, cand1)

            if cand2 and cand2 not in seen:
                seen.add(cand2)
                heappush(minHeap, cand2)

        return res


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    expected_result = [[1, 2], [1, 4], [1, 6]]
    # Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],
    # [7,4],[11,2],[7,6],[11,4],[11,6]
    assert solution.kSmallestPairs(nums1, nums2, k) == expected_result

    # Example 2:
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    expected_result = [[1, 1], [1, 1]]
    # Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],
    # [1,3],[2,3]
    assert solution.kSmallestPairs(nums1, nums2, k) == expected_result

    # Example 3:
    nums1 = [1, 2]
    nums2 = [3]
    k = 3
    expected_result = [[1, 3], [2, 3]]
    # Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
    assert solution.kSmallestPairs(nums1, nums2, k) == expected_result
