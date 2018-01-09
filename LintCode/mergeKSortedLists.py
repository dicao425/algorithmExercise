#!/usr/bin/python
import sys

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        # heap
        # find - O(1)  push - O(logN)  pop - O(logN)  remove - O(logN)  top - O(1)
        import heapq
        heap = []
        for l in lists:
            if l:
                # Heap sorted by the first element of tuple
                heapq.heappush(heap, (l.val, l))
        dummy = ListNode(0)
        p = dummy
        while heap:
            p.next = heapq.heappop(heap)[1]
            p = p.next
            if p.next:
                heapq.heappush(heap, (p.next.val, p.next))
        return dummy.next

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())