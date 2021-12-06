"""
Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer
Matrix mat where mat[i][j] == i * j (1-indexed).
Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.

This is a Matrix that looks like:
1 2 3
2 4 6
3 6 9

Which flattens to the array -> 1 2 2 3 3 4 6 6 9
THe 5th smallest is 3.

"""


class Solution:

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(num) -> bool:
            count = 0
            for val in range(1, m + 1):  # count row by row
                add = min(num // val, n)
                if add == 0:  # early exit
                    break
                count += add
            return count >= k

        left, right = 1, n * m
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":

    solution = Solution()
    m = 3
    n = 3
    k = 5
    print(solution.findKthNumber(m, n, k))