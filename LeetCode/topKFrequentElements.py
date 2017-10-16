#!/usr/bin/python
import sys
import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # it's nlogn  most common is using nlarge of heapq
        return [i[0] for i in collections.Counter(nums).most_common(k)]


def main():
    aa = Solution()
    print aa.topKFrequent()
    return 0

if __name__ == "__main__":
    sys.exit(main())
