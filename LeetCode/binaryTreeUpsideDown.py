#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        curr = root
        pre = None
        nex = None
        tmp = None
        while curr:
            nex = curr.left
            curr.left = tmp
            tmp = curr.right
            curr.right = pre
            pre = curr
            curr = nex
        return pre


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())