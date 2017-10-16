#!/usr/bin/python
import sys


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa = headA
        pb = headB
        if pa is None or pb is None:
            return None
        taila = None
        tailb = None
        while True:
            if pa is None:
                pa = headB
            if pb is None:
                pb = headA
            if pa.next is None:
                taila = pa
            if pb.next is None:
                tailb = pb
            if taila is not None and tailb is not None and taila != tailb:
                return None
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None



def main():
    aa = Solution()
    print aa.getIntersectionNode()
    return 0

if __name__ == "__main__":
    sys.exit(main())
