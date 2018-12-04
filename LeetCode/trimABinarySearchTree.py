#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        self.l = L
        self.r = R
        return self.trim(root)

    def trim(self, node):
        if not node:
            return
        if node.val > self.r:
            return self.trim(node.left)
        elif node.val < self.l:
            return self.trim(node.right)
        else:
            node.left = self.trim(node.left)
            node.right = self.trim(node.right)
            return node


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())