#!/usr/bin/python
import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        while head:
            temp = newHead
            newHead = head
            head = head.next
            newHead.next = temp
        return newHead

def main():
    aa = Solution()
    print aa.reverseList()
    return 0

if __name__ == "__main__":
    sys.exit(main())





class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        while head:
            t = h.next
            h.next = head
            head = head.next
            h.next.next = t
        return h.next
