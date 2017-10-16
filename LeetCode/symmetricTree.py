#!/usr/bin/python
import sys
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if r is None and l is None:
                continue
            if r is None or l is None:
                return False
            if r.val == l.val:
                stack.append((l.left, r.right))
                stack.append((l.right, r.left))
            else:
                return False
        return True


def main():
    aa = Solution()
    print aa.isSymmetric()
    return 0

if __name__ == "__main__":
    sys.exit(main())
