#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkBalanced(root)[1]

    def checkBalanced(self, node):
        if not node:
            return 1, True
        ln, bl = self.checkBalanced(node.left)
        rn, br = self.checkBalanced(node.right)
        b = abs(ln - rn) <= 1
        return max(ln, rn)+1, br and bl and b

def main():
    aa = Solution()
    print aa.isBalanced()
    return 0

if __name__ == "__main__":
    sys.exit(main())
