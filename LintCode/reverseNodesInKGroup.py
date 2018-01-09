#!/usr/bin/python
import sys

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    @param: head: a ListNode
    @param: k: An integer
    @return: a ListNode
    """

    def reverseKGroup(self, head, k):
        # write your code here
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while start.next:
            end = start
            for i in range(k - 1):
                end = end.next
                if not end.next:
                    return dummy.next
            res = self.reverse(start.next, end.next)
            start.next = res[0]
            start = res[1]
        return dummy.next

    def reverse(self, start, end):
        dummy = ListNode(0)
        dummy.next = start
        while dummy.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
        return [end, start]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())