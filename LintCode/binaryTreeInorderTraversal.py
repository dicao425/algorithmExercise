#!/usr/bin/python
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node:
            return

        self.dfs(node.left)
        self.result.append(node.val)
        self.dfs(node.right)
        return


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())