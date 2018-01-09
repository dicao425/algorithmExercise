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
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if not head:
            return head
        ah = ListNode(0)
        bh = ListNode(0)
        atail = ah
        btail = bh
        while head:
            if head.val < x:
                atail.next = head
                atail = atail.next
            else:
                btail.next = head
                btail = btail.next
            head = head.next
        btail.next = None
        atail.next = bh.next
        return ah.next

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())