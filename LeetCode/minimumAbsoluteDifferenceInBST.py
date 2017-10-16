#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = float('inf')
        self.pre = None
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.left)
        if self.pre is not None:
            self.result = min(self.result, node.val - self.pre)
        self.pre = node.val
        self.dfs(node.right)
        return

def main():
    aa = Solution()
    print aa.getMinimumDifference(root)
    return 0

if __name__ == "__main__":
    sys.exit(main())
