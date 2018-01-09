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
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root):
        self.average = 0
        self.node = None
        self.dfs(root)
        return self.node

    def dfs(self, node):
        if node is None:
            return 0, 0
        left_sum, left_size = self.dfs(node.left)
        right_sum, right_size = self.dfs(node.right)
        sum = left_sum + right_sum + node.val
        size = left_size + right_size + 1
        if self.node is None or sum * 1.0 / size > self.average:
            self.node = node
            self.average = sum * 1.0 / size
        return sum, size

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())