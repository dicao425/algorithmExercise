#!/usr/bin/python
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        self.min_sum = None
        self.node = None
        self.dfs(root)
        return self.node

    def dfs(self, node):
        if node is None:
            return 0
        left_sum = self.dfs(node.left)
        right_sum = self.dfs(node.right)
        sum = left_sum + right_sum + node.val
        if not self.node or sum < self.min_sum:
            self.min_sum = sum
            self.node = node
        return sum


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())