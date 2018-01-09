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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        self.result = []
        self.t = target
        self.dfs(root, [])
        return self.result

    def dfs(self, node, path):
        if not node:
            return
        if not node.right and not node.left:
            tmp = path + [node.val]
            if sum(tmp) == self.t:
                self.result.append(tmp)
            return
        path.append(node.val)
        if node.right:
            self.dfs(node.right, path)
        if node.left:
            self.dfs(node.left, path)
        path.pop()

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())