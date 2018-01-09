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
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        self.result = []
        self.dfs(root, "")
        return self.result

    def dfs(self, node, path):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.result.append((path + "->{}".format(node.val))[2:])
            return
        if node.left:
            self.dfs(node.left, path + "->{}".format(node.val))
        if node.right:
            self.dfs(node.right, path + "->{}".format(node.val))
        return

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())