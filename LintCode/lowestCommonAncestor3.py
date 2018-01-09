#!/usr/bin/python
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        if not root:
            return
        stack = [root]
        parent = {root: None}
        while stack and (A not in parent or B not in parent):
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        if A not in parent or B not in parent:
            return
        ancestor = set()
        while A:
            ancestor.add(A)
            A = parent[A]
        while B not in ancestor:
            B = parent[B]
        return B

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())