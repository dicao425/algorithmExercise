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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum2(self, root, target):
        # write your code here
        self.result = []
        if not root:
            return []
        self.t = target
        self.dfs(root, [])
        return self.result

    def dfs(self, node, path):
        if not node:
            return
        path.append(node.val)
        s = 0
        for i in range(len(path) - 1, -1, -1):
            s += path[i]
            if s == self.t:
                self.result.append(path[i:])
        self.dfs(node.right, path)
        self.dfs(node.left, path)
        path.pop()


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())