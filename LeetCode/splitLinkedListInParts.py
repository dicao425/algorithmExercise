#!/usr/bin/python
import sys

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        curr = root
        l = 0
        while curr:
            l += 1
            curr = curr.next
        width, reminder = divmod(l, k)
        result = []
        curr = root
        for i in range(k):
            head = curr
            for j in range(width + (i < reminder) - 1):
                if curr:
                    curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
            result.append(head)
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())