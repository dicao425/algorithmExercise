#!/usr/bin/python
import sys


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        n = node.right
        while n:
            self.stack.append(n)
            n = n.left
        return node.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


def main():
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)
    a6 = TreeNode(6)
    a7 = TreeNode(7)
    a4.left = a2
    a4.right = a6
    a2.left = a1
    a2.right = a3
    a6.left = a5
    a6.right = a7
    aa = BSTIterator(a4)
    import pdb
    pdb.set_trace()
    return 0

if __name__ == "__main__":
    sys.exit(main())