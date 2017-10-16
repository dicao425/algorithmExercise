#!/usr/bin/python
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.result = []
        self.sum = sum
        self.dfs(root, [])
        return self.result

    def dfs(self, node, l):
        if not node.left and not node.right:
            if sum(l) + node.val == self.sum:
                self.result.append(l + [node.val])
            return
        if node.left:
            self.dfs(node.left, l + [node.val])
        if node.right:
            self.dfs(node.right, l + [node.val])
        return


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())