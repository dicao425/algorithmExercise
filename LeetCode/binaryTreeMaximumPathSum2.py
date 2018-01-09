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
    @param: root: the root of binary tree.
    @return: An integer
    """

    def maxPathSum2(self, root):
        # write your code here
        if not root:
            return 0
        self.result = root.val
        self.dfs(root, 0)
        return self.result

    def dfs(self, node, s):
        if not node:
            return
        self.result = max(self.result, s + node.val)
        self.dfs(node.right, s + node.val)
        self.dfs(node.left, s + node.val)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())