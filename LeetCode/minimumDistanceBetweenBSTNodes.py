#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = float('inf')
        self.inorder = []
        self.dfs(root)
        if len(self.inorder) == 1:
            return 0
        for i in range(1, len(self.inorder)):
            self.result = min(self.inorder[i] - self.inorder[i - 1], self.result)
        return self.result

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.inorder.append(node.val)
        self.dfs(node.right)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())