#!/usr/bin/python
import sys


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if head.next is None or k == 0:
            return head
        length = 0
        tail = None
        p = head
        while p:
            if p.next is None:
                tail = p
            p = p.next
            length += 1
        k = k % length
        if k == 0:
            return head
        p1 = head
        p2 = head
        for i in range(k):
            p1 = p1.next
        while p1.next:
            p2 = p2.next
            p1 = p1.next
        tmp = p2.next
        p1.next = head
        p2.next = None
        head = tmp
        return head


def main():
    aa = Solution()
    print aa.rotateRight()
    return 0

if __name__ == "__main__":
    sys.exit(main())
