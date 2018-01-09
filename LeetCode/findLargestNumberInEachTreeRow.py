#!/usr/bin/python
import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        rows = []
        q = [(0, root)]
        while q:
            l, c = q.pop(0)
            if len(rows) < l+1:
                rows.append([])
            rows[l].append(c.val)
            if c.left:
                q.append((l+1, c.left))
            if c.right:
                q.append((l+1, c.right))
        result = []
        for i in rows:
            result.append(max(i))
        return result

def main():
    aa = Solution()
    print aa.largestValues()
    return 0

if __name__ == "__main__":
    sys.exit(main())
