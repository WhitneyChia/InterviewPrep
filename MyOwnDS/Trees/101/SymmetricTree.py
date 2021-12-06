"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.two_nodes_the_same(root, root)

    def two_nodes_the_same(self, first_node, second_node):
        if not first_node and not second_node:
            return True
        if not first_node or not second_node:
            return False
        if first_node.val != second_node.val:
            return False
        if first_node.val == second_node.val:
            return self.two_nodes_the_same(first_node.left, second_node.right) and self.two_nodes_the_same(
                first_node.right, second_node.left)
