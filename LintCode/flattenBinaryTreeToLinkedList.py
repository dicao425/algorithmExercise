#!/usr/bin/python
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return:
    """

    def flatten(self, root):
        # write your code here
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.left = None
            if not stack:
                node.right = None
            else:
                node.right = stack[-1]


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())