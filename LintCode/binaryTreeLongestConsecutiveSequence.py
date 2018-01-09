#!/usr/bin/python
import sys

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive(self, root):
        # write your code here
        if not root:
            return 0
        self.result = 1
        self.dfs(root, 1)
        return self.result

    def dfs(self, node, l):
        if not node:
            return
        if node.right:
            if node.val + 1 == node.right.val:
                tmp = l + 1
                self.result = max(self.result, tmp)
            else:
                tmp = 1
            self.dfs(node.right, tmp)
        if node.left:
            if node.val + 1 == node.left.val:
                tmp = l + 1
                self.result = max(self.result, tmp)
            else:
                tmp = 1
            self.dfs(node.left, tmp)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())