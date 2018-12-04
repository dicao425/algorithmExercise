#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        l = max(left, right)
        if l < len(self.result):
            self.result[l].append(node.val)
        else:
            self.result.append([node.val])
        return l + 1


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())