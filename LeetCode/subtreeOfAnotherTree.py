#!/usr/bin/python
import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def post_order(node):
            if node is None:
                return '$'
            l = post_order(node.left)
            r = post_order(node.right)
            return l + r + str(node.val) + '^'
        return post_order(t) in post_order(s)

def main():
    aa = Solution()
    print aa.isSubtree()
    return 0

if __name__ == "__main__":
    sys.exit(main())
