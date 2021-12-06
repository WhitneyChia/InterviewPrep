"""
https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are
directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""
from typing import List


class Solution:
    """ This is similar to the friends circle problem, just visualize as a graph and run dfs"""
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        This is essentially finding the number of components of a graph.
        We are given an adjacency matrix to represent the graph
        """

        # First define the number of cities
        num_cities = len(isConnected)

        # Initialize the number of provinces
        provinces = 0

        # Track the cities that have been visited already, initialize as visited nothing
        visited_cities = [False for i in range(num_cities)]

        # dfs call
        def dfs(city):
            visited_cities[city] = True
            for dest_city in range(num_cities):
                if not visited_cities[dest_city] and isConnected[city][dest_city]:
                    dfs(dest_city)

        # Iterate through adj matrix, calling dfs on each and updating visited
        # For each new city that we haven't visited yet, provinces goes up by 1
        for city in range(len(isConnected)):
            if not visited_cities[city]:
                dfs(city)
                provinces += 1

        return provinces


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    expected_result = 2
    assert solution.findCircleNum(isConnected) == expected_result

    # Example 2:
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    expected_result = 3
    assert solution.findCircleNum(isConnected) == expected_result

    # Example 3:
    isConnected = M = [[1, 1, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0],
                       [0, 0, 1, 1, 1, 0],
                       [0, 0, 1, 1, 0, 0],
                       [0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1]]

    expected_result = 3
    assert solution.findCircleNum(isConnected) == expected_result
