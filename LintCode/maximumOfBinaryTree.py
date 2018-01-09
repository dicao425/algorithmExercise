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
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth1(self, root):
        # DFS
        self.result = 0
        self.dfs(root, 0)
        return self.result

    def dfs(self, node, depth):
        if not node:
            self.result = max(self.result, depth)
            return
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)

    def maxDepth2(self, root):
        # Divid & Conquer
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def maxDepth(self, root):
        # Non-recursion
        if not root:
            return 0
        stack = [(root, 0)]
        result = 0
        while stack:
            node, depth = stack.pop()
            if not node:
                result = max(result, depth)
            else:
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())