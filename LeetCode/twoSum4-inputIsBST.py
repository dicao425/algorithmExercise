#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        hs = set()
        return self.f(root, k, hs)

    def f(self, node, k, hs):
        if not node:
            return False
        if k - node.val in hs:
            return True
        hs.add(node.val)
        return self.f(node.left, k, hs) or self.f(node.right, k, hs)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())