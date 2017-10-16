#!/usr/bin/python
import sys


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode

        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        nh = ListNode(0)
        nh.next = head
        rh = nh
        for i in range(m-1):
            rh = rh.next
        rt = rh.next
        for i in range(n-m):
            curr = rt.next
            t_temp = curr.next
            curr.next = rh.next
            rh.next = curr
            rt.next = t_temp
        return nh.next


def main():
    aa = Solution()
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)
    ll.next.next.next.next.next = ListNode(6)
    qq= aa.reverseBetween(ll, 2, 4)
    while qq:
        print qq.val
        qq=qq.next


    return 0

if __name__ == "__main__":
    sys.exit(main())
