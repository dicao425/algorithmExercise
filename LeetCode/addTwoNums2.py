#!/usr/bin/python
import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = []
        n2 = []
        while l1:
            n1.append(str(l1.val))
            l1 = l1.next
        while l2:
            n2.append(str(l2.val))
            l2 = l2.next
        num = str(int(''.join(n1)) + int(''.join(n2)))
        dummy = ListNode(0)
        p = dummy
        for i in range(len(num)):
            p.next = ListNode(num[i])
            p = p.next
        return dummy.next

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())