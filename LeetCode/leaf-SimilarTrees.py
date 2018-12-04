#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.tree1 = []
        self.tree2 = []
        self.leaf(root1, self.tree1)
        self.leaf(root2, self.tree2)
        return self.tree1 == self.tree2

    def leaf(self, node, result):
        if not node:
            return
        if not node.left and not node.right:
            result.append(node.val)
            return
        self.leaf(node.right, result)
        self.leaf(node.left, result)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())