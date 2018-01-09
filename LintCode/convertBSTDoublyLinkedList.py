#!/usr/bin/python
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""


class Solution:
    """
    @param: root: The root of tree
    @return: the head of doubly list node
    """

    def bstToDoublyList(self, root):
        # write your code here
        if not root:
            return
        root_ln = self.dfs(root)
        while root_ln.prev:
            root_ln = root_ln.prev
        return root_ln

    def dfs(self, node):
        if not node:
            return
        ln = DoublyListNode(node.val)
        left_ln = self.dfs(node.left)
        if left_ln:
            while left_ln.next:
                left_ln = left_ln.next
            left_ln.next = ln
            ln.prev = left_ln
        right_ln = self.dfs(node.right)
        if right_ln:
            while right_ln.prev:
                right_ln = right_ln.prev
            right_ln.prev = ln
            ln.next = right_ln
        return ln


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())