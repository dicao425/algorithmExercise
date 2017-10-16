#!/usr/bin/python
import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.right is None or root.left is None:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

def main():
    aa = Solution()
    print aa.minDepth()
    return 0

if __name__ == "__main__":
    sys.exit(main())
