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
        lh = tail = TreeLinkNode(0)
        while root:
            tail.next = root.left  # level header will have the same next will tail, they have relations
            if tail.next:
                tail = tail.next  # if do this, tail will lost the relationship with level head
            tail.next = root.right
            if tail.next:
                tail = tail.next
            root = root.next
            if not root:
                tail = lh  # level head always stores the first non-None
                root = lh.next


def main():
    r1 = TreeLinkNode(1)
    r2 = TreeLinkNode(2)
    r3 = TreeLinkNode(3)
    r4 = TreeLinkNode(4)
    r5 = TreeLinkNode(5)
    r6 = TreeLinkNode(6)
    r1.left = r2
    r1.right = r3
    r2.left = r4
    r2.right = r5
    r3.right = r6
    aa = Solution()
    aa.connect(r1)
    return 0

if __name__ == "__main__":
    sys.exit(main())