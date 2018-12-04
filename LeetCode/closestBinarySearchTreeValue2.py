#!/usr/bin/python
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        result = []
        s1 = []     # stack predecessors
        s2 = []     # stack successors
        self.inorder(root, target, False, s1)
        self.inorder(root, target, True, s2)
        while k > 0:
            if not s1:
                result.append(s2.pop())
            elif not s2:
                result.append(s1.pop())
            elif abs(s1[-1] - target) < abs(s2[-1] - target):
                result.append(s1.pop())
            else:
                result.append(s2.pop())
            k -= 1
        return result


    def inorder(self, root, target, reverse, stack):
        if not root:
            return
        self.inorder(root.right if reverse else root.left, target, reverse, stack)
        if (reverse and root.val <= target) or (not reverse and root.val > target):
            return
        stack.append(root.val)
        self.inorder(root.left if reverse else root.right, target, reverse, stack)




def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())