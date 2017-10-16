#!/usr/bin/python
import sys


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        nh = ListNode(0)
        nh.next = head
        c = nh
        p = head
        while p:
            if p.val != p:
                c.next = p
                c = c.next
            p = p.next
        c.next = None
        return nh.next


def main():
    aa = Solution()
    print aa.removeElements()
    return 0

if __name__ == "__main__":
    sys.exit(main())
