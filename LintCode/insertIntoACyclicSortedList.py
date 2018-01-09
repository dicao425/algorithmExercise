#!/usr/bin/python
import sys

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here
        if node is None:
            node = ListNode(x)
            node.next = node
            return node
        p = node
        pre = None
        while True:
            pre = p
            p = p.next
            if p is node:
                break
            if pre.val <= x <= p.val:
                break
            if pre.val > p.val and (p.val > x or pre.val < x):
                break
        n = ListNode(x)
        pre.next = n
        n.next = p
        return n

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())