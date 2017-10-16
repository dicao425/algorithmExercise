#!/usr/bin/python
import sys

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

def main():
    aa = Solution()
    print aa.intersection([1,2,3], [2])
    return 0

if __name__ == "__main__":
    sys.exit(main())
