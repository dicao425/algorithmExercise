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
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        new_len = len(hashTable)*2
        new_hash = [None for _ in range(new_len)]
        for item in hashTable:
            p = item
            while p:
                pos = p.val % new_len
                if new_hash[pos]:
                    cur = new_hash[pos]
                    while cur.next:
                        cur = cur.next
                    cur.next = ListNode(p.val)
                else:
                    new_hash[pos] = ListNode(p.val)
                p = p.next
        return new_hash

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())