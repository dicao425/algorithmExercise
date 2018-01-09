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
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root:
            return
        suc = None
        while root and root.val != p.val:
            if root.val > p.val:
                suc = root
                root = root.left
            else:
                root = root.right
        if not root:
            return
        if not root.right:
            return suc
        else:
            root = root.right
            while root.left:
                root = root.left
        return root

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())