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
        :rtype: int
        """
        self.sum = sum
        self.result = 0
        if not root:
            return 0
        self.dfs(root, [])
        return self.result

    def dfs(self, node, vl):
        if not node:
            return
        vl = [i + node.val for i in vl] + [node.val]
        print vl
        if self.sum in vl:
            self.result += 1
        self.dfs(node.left, vl)
        self.dfs(node.right, vl)
        return

def main():
    tt = TreeNode(5)
    tt.left = TreeNode(4)
    tt.left.left = TreeNode(11)
    tt.left.left.left = TreeNode(7)
    tt.left.left.right = TreeNode(2)
    tt.right = TreeNode(8)
    tt.right.left = TreeNode(13)
    tt.right.right = TreeNode(4)
    tt.right.right.left = TreeNode(5)
    tt.right.right.right = TreeNode(1)
    aa = Solution()
    print aa.pathSum(tt, 22)
    return 0

if __name__ == "__main__":
    sys.exit(main())
