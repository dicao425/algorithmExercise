#!/usr/bin/python
import sys
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[k-1]


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())