#!/usr/bin/python
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        return self.dfs(root, 0)[1]

    def dfs(self, node, depth):
        if node is None:
            return depth, True
        l_depth, lb = self.dfs(node.left, depth + 1)
        r_depth, rb = self.dfs(node.right, depth + 1)
        if not lb or not rb or abs(l_depth - r_depth) > 1:
            return max(l_depth, r_depth), False
        return max(l_depth, r_depth), True

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())