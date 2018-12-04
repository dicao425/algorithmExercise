#!/usr/bin/python
import sys

import heapq

#Takes O(m + k*log(m)) time and O(m) extra space.

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        q = []

        def push_to_heap(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(q, (nums1[i] + nums2[j], i, j))

        result = []
        push_to_heap(0, 0)
        while q and len(result) < k:
            s, i, j = heapq.heappop(q)
            result.append([nums1[i], nums2[j]])
            push_to_heap(i, j + 1)
            if j == 0:
                push_to_heap(i + 1, j)
        return result


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())