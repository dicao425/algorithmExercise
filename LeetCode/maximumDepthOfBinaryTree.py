#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # self.max_depth = 0
        # self.dfs(root, 0)
        # return self.max_depth
        return self.recursive(root)

    def dfs(self, node, depth):
        if not node:
            self.max_depth = max(self.max_depth, depth)
            return
        depth += 1
        self.dfs(node.left, depth)
        self.dfs(node.right, depth)
        return

    def recursive(self, root):
        stack = [(root, 0)]
        m = 0
        while stack:
            node, depth = stack.pop()
            if not node:
                m = max(m, depth)
            else:
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return m

def main():
    aa = Solution()
    print aa.maxDepth()
    return 0

if __name__ == "__main__":
    sys.exit(main())
