#!/usr/bin/python
import sys


#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node:
            return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.result = max(self.result, l + r)
        return max(l, r) + 1


def main():
    aa = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(4)
    t.left.right = TreeNode(5)
    print aa.diameterOfBinaryTree(t)
    return 0

if __name__ == "__main__":
    sys.exit(main())
