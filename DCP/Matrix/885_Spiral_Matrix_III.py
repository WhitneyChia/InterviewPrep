"""
https://leetcode.com/problems/spiral-matrix-iii/

You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row
and column in the grid, and the southeast corner is at the last row and column.
You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the
grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.).
Eventually, we reach all rows * cols spaces of the grid.
Return an array of coordinates representing the positions of the grid in the order you visited them.

Example 1:
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
"""


class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        ans = [(r0, c0)]
        if R * C == 1: return ans

        # For walk length k = 1, 3, 5 ...
        for k in range(1, 2*(R+C), 2):

            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):

                # For each of dk units in the current direction ...
                for _ in range(dk):

                    # Step in that direction
                    r0 += dr
                    c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans


if __name__ == "__main__":

    solution = Solution()
    rows = 1
    cols = 4
    rStart = 0
    cStart = 0
    assert solution.spiralMatrixIII(rows, cols, rStart, cStart) == [(0, 0), (0, 1), (0, 2), (0, 3)]

    solution = Solution()
    rows = 5
    cols = 6
    rStart = 1
    cStart = 4
    assert solution.spiralMatrixIII(rows, cols, rStart, cStart) == [(1, 4), (1, 5), (2, 5), (2, 4), (2, 3), (1, 3),
                                                                    (0, 3), (0, 4), (0, 5), (3, 5), (3, 4), (3, 3),
                                                                    (3, 2), (2, 2), (1, 2), (0, 2), (4, 5), (4, 4),
                                                                    (4, 3), (4, 2), (4, 1), (3, 1), (2, 1), (1, 1),
                                                                    (0, 1), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)]
