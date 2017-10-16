#!/usr/bin/python
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.result = []
        self.dfs(root)
        p = 0
        for i in range(1, len(self.result)):
            if self.result[i] <= self.result[p]:
                return False
            p += 1
        return True

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.result.append(node.val)
        self.dfs(node.right)
        return



def main():
    aa = Solution()
    print aa.isValidBST()
    return 0

if __name__ == "__main__":
    sys.exit(main())
