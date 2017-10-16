#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.get_result(root, None)

    def get_result(self, node, end):
        if not node:
            return end
        node.right = self.get_result(node.left, self.get_result(node.right, end))
        node.left = None
        return node

def main():
    aa = Solution()
    print aa.flatten()
    return 0

if __name__ == "__main__":
    sys.exit(main())
