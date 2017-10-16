#!/usr/bin/python
import sys

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        d = {}
        for i in nums1:
            d[i] = d.get(i, 0) + 1
        for i in nums2:
            if i in d and d[i] > 0:
                result.append(i)
                d[i] -= 1
        return result

def main():
    aa = Solution()
    print aa.intersect()
    return 0

if __name__ == "__main__":
    sys.exit(main())
