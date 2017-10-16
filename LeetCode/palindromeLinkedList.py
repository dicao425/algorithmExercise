#!/usr/bin/python
import sys

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next
        n = None
        while s:
            t = s.next
            s.next = n
            n = s
            s = t
        while head and n:
            if n.val != head.val:
                return False
            n = n.next
            head = head.next
        return True

def main():
    aa = Solution()
    print aa.isPalindrome()
    return 0

if __name__ == "__main__":
    sys.exit(main())
