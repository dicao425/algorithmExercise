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
    @param: root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        self.result = float('inf')
        self.dfs(root, 1)
        return self.result

    def dfs(self, node, d):
        if not node:
            return
        if not node.right and not node.left:
            self.result = min(self.result, d)
            return
        self.dfs(node.right, d + 1)
        self.dfs(node.left, d + 1)
        return

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())