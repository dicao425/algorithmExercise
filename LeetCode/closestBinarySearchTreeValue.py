#!/usr/bin/python
import sys


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        result = root.val
        while root:
            if abs(root.val - target) < abs(result - target):
                result = root.val
            root = root.left if target < root.val else root.right
        return result



class Solution1:
    def closestValue(self, root, target):
        if not root:
            return
        lower = self.findLower(root, target)
        upper = self.findUpper(root, target)
        if lower and upper:
            if target - lower.val > upper.val - target:
                return upper.val
            else:
                return lower.val
        if lower:
            return lower.val
        if upper:
            return upper.val


    def findLower(self, root, target):
        cur = root
        last = None
        while cur:
            if cur.val <= target:
                last = cur
                cur = cur.right
            else:
                cur = cur.left
        return last


    def findUpper(self, root, target):
        cur = root
        last = None
        while cur:
            if cur.val > target:
                last = cur
                cur = cur.left
            else:
                cur = cur.right
        return last


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())