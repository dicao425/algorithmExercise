#!/usr/bin/python
import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while (root.val - p.val)*(root.val - q.val) > 0:
            root = (root.left, root.right)[root.val>p.val]
        return root

def main():
    aa = Solution()
    print aa.lowestCommonAncestor()
    return 0

if __name__ == "__main__":
    sys.exit(main())
