
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_order_traversal(root: TreeNode):
    if root:
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def in_order_traversal(root: TreeNode):
    if root:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)


def post_order_traversal(root: TreeNode):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val)


def recursive_level_order_traversal(root: TreeNode):
    levels = []
    if not root:
        return levels

    def helper(node, level):
        # start the current level
        if len(levels) == level:
            levels.append([])

        # append the current node value
        levels[level].append(node.val)

        # process child nodes for the next level
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)

    helper(root, 0)
    return levels


def level_order_traversal(root: TreeNode):
    """
    Essentially breadth first search on a tree, trees are just a special kind of graph
    """
    h = height(root)
    for i in range(1, h + 1):
        print_current_level(root, i)


# Print nodes at a current level
def print_current_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1:
        print_current_level(root.left, level - 1)
        print_current_level(root.right, level - 1)


""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


if __name__ == "__main__":

    #       1
    #   2      3
    # 4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    pre_order_traversal(root)

    print("\n")

    in_order_traversal(root)

    print("\n")

    post_order_traversal(root)

    print("\n")

    level_order_traversal(root)

    print("\n")

    print(recursive_level_order_traversal(root))