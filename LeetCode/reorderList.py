#!/usr/bin/python
import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        if not head.next:
            return head
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        slow.next = None
        mhead = ListNode(0)
        mhead.next = tmp
        while tmp.next:
            t = tmp.next
            h = mhead.next
            mhead.next = t
            tmp.next = t.next
            t.next = h
        h1 = head
        h2 = mhead.next
        while h1.next and h2.next:
            t1 = h1.next
            t2 = h2.next
            h1.next = h2
            h2.next = t1
            h1 = t1
            h2 = t2
        if h2:
            h1.next = h2
        return head

def main():
    pp = ListNode(1)
    pp.next = ListNode(2)
    pp.next.next = ListNode(3)
    pp.next.next.next = ListNode(4)
    pp.next.next.next.next = ListNode(5)
    pp.next.next.next.next.next = ListNode(6)
    pp.next.next.next.next.next.next = ListNode(7)
    aa = Solution()
    kk=aa.reorderList(pp)
    while kk:
        print kk.val
        kk=kk.next
    return 0

if __name__ == "__main__":
    sys.exit(main())