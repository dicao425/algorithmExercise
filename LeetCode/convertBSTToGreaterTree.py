#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.vals = []
        self.s = 0
        self.dfs1(root)
        self.dfs2(root)
        return root

    def dfs1(self, node):
        if node:
            self.dfs1(node.left)
            self.vals.append(node.val)
            self.dfs1(node.right)

    def dfs2(self, node):
        if node:
            self.dfs2(node.right)
            self.s += self.vals.pop()
            node.val = self.s
            self.dfs2(node.left)

# traverse 1: inorder -> list from small to big
# traverse 2: reverse inorder , gen the new tree

def main():
    aa = Solution()
    print aa.convertBST()
    return 0

if __name__ == "__main__":
    sys.exit(main())
