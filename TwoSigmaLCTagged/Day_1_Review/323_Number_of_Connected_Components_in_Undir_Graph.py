"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi]
indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
"""
from typing import List


class Solution:
    def dfs(self, i, adjacency_list, visited_nodes):
        for child_node in adjacency_list[i]:
            if child_node not in visited_nodes:
                visited_nodes.add(child_node)
                self.dfs(child_node, adjacency_list, visited_nodes)

    def find_adjacency_list(self, edges, n):
        """ Simply converts the given list into an adjacency list """
        adjacency_list = [[] for _ in range(n)]
        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)
        return adjacency_list

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_components = 0
        visited_nodes = set()
        adjacency_list = self.find_adjacency_list(edges, n)
        for i in range(n):
            if i not in visited_nodes:
                self.dfs(i, adjacency_list, visited_nodes)
                num_components += 1

        return num_components


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    expected_result = 2
    assert solution.countComponents(n, edges) == expected_result

    # Example 2:
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    expected_result = 1
    assert solution.countComponents(n, edges) == expected_result
