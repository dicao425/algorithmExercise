#!/usr/bin/python
import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            idx = inorder.index(postorder.pop())
            node = TreeNode(inorder[idx])
            node.right = self.buildTree(inorder[idx+1:], postorder)
            node.left = self.buildTree(inorder[:idx], postorder)
            return node
def main():
    aa = Solution()
    print aa.buildTree()
    return 0

if __name__ == "__main__":
    sys.exit(main())
