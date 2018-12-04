#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = float('inf')
        self.root = root.val
        self.dfs(root)
        return self.result if self.result != float('inf') else -1

    def dfs(self, node):
        if not node:
            return
        if self.root < node.val < self.result:
            self.result = node.val
        self.dfs(node.left)
        self.dfs(node.right)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())