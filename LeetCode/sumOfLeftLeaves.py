#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            return True
        if self.dfs(node.left):
            self.result += node.left.val
        self.dfs(node.right)
        return

def main():
    aa = Solution()
    print aa.sumOfLeftLeaves(root)
    return 0

if __name__ == "__main__":
    sys.exit(main())
