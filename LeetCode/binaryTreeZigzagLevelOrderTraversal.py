#!/usr/bin/python
import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        result = []
        f = 1
        while stack:
            t = []
            for i in range(len(stack)):
                node = stack.pop(0)
                t.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            result.append(t[::f])
            f = -f
        return result

def main():
    aa = Solution()
    print aa.zigzagLevelOrder()
    return 0

if __name__ == "__main__":
    sys.exit(main())
