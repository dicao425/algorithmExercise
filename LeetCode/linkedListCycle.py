#!/usr/bin/python
import sys

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        l, f = head, head
        while f.next and f.next.next:
            l = l.next
            f = f.next.next
            if l == f:
                return True
        return False

def main():
    aa = Solution()
    print aa.hasCycle()
    return 0

if __name__ == "__main__":
    sys.exit(main())
