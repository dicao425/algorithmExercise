#!/usr/bin/python
import sys

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        d = {}
        p = head
        while p:
            d[p] = RandomListNode(p.label)
            p = p.next
        p = head
        while p:
            d[p].next = d.get(p.next)
            d[p].random = d.get(p.random)
            p = p.next
        return d.get(head)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())