#!/usr/bin/python
import sys


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return self.merge(head1, head2)

    def merge(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        dummy = ListNode(0)
        p = dummy
        while head1 and head2:
            if head1.val > head2.val:
                p.next = head2
                head2 = head2.next
                p = p.next
            else:
                p.next = head1
                head1 = head1.next
                p = p.next
        if head1 is None:
            p.next = head2
        if head2 is None:
            p.next = head1
        return dummy.next

def main():
    aa = Solution()
    print aa.sortList()
    return 0

if __name__ == "__main__":
    sys.exit(main())
