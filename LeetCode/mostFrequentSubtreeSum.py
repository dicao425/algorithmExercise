#!/usr/bin/python
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = {}
        self.dfs(root)
        m = max(self.result.values())
        return [i for i in self.result if self.result[i] == m]

    def dfs(self, node):
        if not node:
            return 0
        s = node.val + self.dfs(node.left) + self.dfs(node.right)
        self.result[s] = self.result.get(s, 0) + 1
        return s

def main():
    n = TreeNode(5)
    n.left = TreeNode(2)
    n.right = TreeNode(-5)
    aa = Solution()
    print aa.findFrequentTreeSum(n)
    return 0

if __name__ == "__main__":
    sys.exit(main())
