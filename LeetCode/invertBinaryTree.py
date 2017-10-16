#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.rdfs(root)
        return root

    def dfs(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.dfs(node.left)
        self.dfs(node.right)
        return

    def rdfs(self, root):
        stack = [root]
        while stack:
            n = stack.pop()
            if n:
                n.left, n.right = n.right, n.left
                stack.append(n.left)
                stack.append(n.right)
        return root

def main():
    aa = Solution()
    print aa.invertTree()
    return 0

if __name__ == "__main__":
    sys.exit(main())
