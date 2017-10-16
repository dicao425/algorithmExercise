#!/usr/bin/python
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(t1, t2)

    def dfs(self, n1, n2):
        if not n1 and not n2:
            return
        nt = TreeNode((n1.val if n1 else 0) + (n2.val if n2 else 0))
        nt.left = self.dfs(n1.left if n1 else None, n2.left if n2 else None)
        nt.right = self.dfs(n1.right if n1 else None, n2.right if n2 else None)
        return nt

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())