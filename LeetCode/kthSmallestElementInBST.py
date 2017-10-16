#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.l = []
        self.inorder(root)
        return self.l[k - 1]

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.l.append(node.val)
        self.inorder(node.right)
        return

def main():
    aa = Solution()
    print aa.kthSmallest()
    return 0

if __name__ == "__main__":
    sys.exit(main())
