#!/usr/bin/python
import sys

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        stack = [(root, 0)]
        level = -1
        while stack:
            n, l = stack.pop(0)
            if l == level:
                h.next = n
                h = h.next
            else:
                h = n
                level += 1
            if n and n.left:
                stack.append((n.left, l + 1))
            if n and n.right:
                stack.append((n.right, l + 1))
        return
def main():
    t1 = TreeLinkNode(1)
    t2 = TreeLinkNode(2)
    t3 = TreeLinkNode(3)
    t4 = TreeLinkNode(4)
    t5 = TreeLinkNode(5)
    t6 = TreeLinkNode(6)
    t7 = TreeLinkNode(7)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    aa = Solution()
    kk = aa.connect(t1)
    import pdb
    pdb.set_trace()
    return 0

if __name__ == "__main__":
    sys.exit(main())