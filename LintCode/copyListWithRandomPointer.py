#!/usr/bin/python
import sys
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
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
        return d[head]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())