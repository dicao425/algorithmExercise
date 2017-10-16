#!/usr/bin/python
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # reverse custom preorder (mid-right-left)
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            n = stack.pop()
            if n:
                result.append(n.val)
                stack.append(n.left)
                stack.append(n.right)
        return result[::-1]


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())