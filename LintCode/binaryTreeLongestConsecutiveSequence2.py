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

    def longestConsecutive2(self, root):
        # write your code here
        return self.dfs(root)[0]

    def dfs(self, node):
        if not node:
            return 0, 0, 0
        left_len, left_down, left_up = self.dfs(node.left)
        right_len, right_down, right_up = self.dfs(node.right)
        down, up = 0, 0
        if node.left and node.left.val + 1 == node.val:
            down = max(down, left_down + 1)
        if node.left and node.left.val - 1 == node.val:
            up = max(up, left_up + 1)
        if node.right and node.right.val + 1 == node.val:
            down = max(down, right_down + 1)
        if node.right and node.right.val - 1 == node.val:
            up = max(up, right_up + 1)
        len = down + 1 + up
        len = max(len, left_len, right_len)
        return len, down, up


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())