#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: an integer array
    @param: k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        # min heap - O(nlogk)
        import heapq
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        heap.sort(reverse=True)
        return heap

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())