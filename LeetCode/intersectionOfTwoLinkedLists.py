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
        if not headA or not headB:
            return
        pa = headA
        pb = headB
        while pa != pb:
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
        return pa


class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return
        pa = headA
        pb = headB
        ta = None
        tb = None
        while True:
            if pa == pb:
                return pa
            if not pa.next:
                ta = pa
            if not pb.next:
                tb = pb
            if ta and tb and ta != tb:
                return
            pa = pa.next
            pb = pb.next
            if not pa:
                pa = headB
            if not pb:
                pb = headA
        return



class Solution2(object):
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
