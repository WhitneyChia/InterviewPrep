"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""


from typing import Optional, List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: TreeNode, res: List):
        if not root:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
