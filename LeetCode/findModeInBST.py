#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.d = {}
        self.dfs(root)
        m = max(self.d.values())
        return [i for i, v in self.d.items() if v == m]

    def dfs(self, node):
        if not node:
            return
        self.d[node.val] = self.d.get(node.val, 0) + 1
        self.dfs(node.left)
        self.dfs(node.right)
        return

def main():
    aa = Solution()
    print aa.findMode()
    return 0

if __name__ == "__main__":
    sys.exit(main())
