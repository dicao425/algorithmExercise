#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: an integer unsorted array
    @param: k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        # write your code here
        # min heap
        import heapq
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())