#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.traverse(p, q)

    def traverse(self, n1, n2):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False
        if n1.val != n2.val:
            return False
        if not self.traverse(n1.left, n2.left):
            return False
        if not self.traverse(n1.right, n2.right):
            return False
        return True

def main():
    aa = Solution()
    print aa.isSameTree()
    return 0

if __name__ == "__main__":
    sys.exit(main())
