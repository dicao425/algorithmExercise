#!/usr/bin/python
import sys

def isBadVersion():
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n
        while first + 1 < last:
            mid = (first+last)/2
            if isBadVersion(mid):
                last = mid
            else:
                first = mid
        if isBadVersion(first):
            return first
        return last

class Solution1(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        h = n
        while l < h:
            m = l + (h - l) // 2
            if isBadVersion(m):
                h = m
            else:
                l = m + 1
        return h



def main():
    aa = Solution()
    print aa.firstBadVersion()
    return 0

if __name__ == "__main__":
    sys.exit(main())
