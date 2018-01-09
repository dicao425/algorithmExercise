#!/usr/bin/python
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST1(self, root):
        # write your code here
        self.inorder = []
        self.dfs(root)
        if not self.inorder or len(self.inorder) == 1:
            return True
        pre = self.inorder[0]
        for i in range(1, len(self.inorder)):
            if self.inorder[i] <= pre:
                return False
            pre = self.inorder[i]
        return True

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.inorder.append(node.val)
        self.dfs(node.right)
        return

    def isValidBST(self, root):
        # Divid and conquer
        return self.dc(root, -float('inf'), float('inf'))

    def dc(self, node, l, r):
        if not node:
            return True
        if node.val <= l or node.val >= r:
            return False
        return self.dc(node.left, l, min(node.val, r)) and self.dc(node.right, max(node.val, l), r)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())