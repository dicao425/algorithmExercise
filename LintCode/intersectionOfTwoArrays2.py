#!/usr/bin/python
import sys


class Solution:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        # write your code here
        d = {}
        result = []
        for n in nums1:
            d[n] = d.get(n, 0) + 1
        for n in nums2:
            if n in d and d[n] != 0:
                result.append(n)
                d[n] -= 1
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())