#!/usr/bin/python
import sys
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nh = head
        if nh is None or nh.next is None:
            return head
        curr = nh.val
        p = nh.next
        while p:
            if p.val != curr:
                curr = p.val
                nh.next.val = curr
                nh = nh.next
            p = p.next
        nh.next = None
        return nh

    def deleteDuplicates(self, head):
        if not head:
            return
        p1 = head
        p2 = head.next
        while p2:
            if p1.val != p2.val:
                p1.next = p2
                p1 = p1.next
            p2 = p2.next
        p1.next = None
        return head

def main():
    aa = Solution()
    print aa.deleteDuplicates()
    return 0

if __name__ == "__main__":
    sys.exit(main())
ƒ