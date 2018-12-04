#!/usr/bin/python
import sys

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = 0
        r = len(A) - 1
        while l + 1 < r:
            m = (l+r) /2
            if A[m] < A[m-1]:
                r = m
            elif A[m] > A[m-1]:
                l = m
            else:
                r = m
        if A[l] > A[r]:
            return l
        return r

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())