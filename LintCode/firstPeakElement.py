#!/usr/bin/python
import sys

class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        first = 1
        last = len(A)-2
        while first + 1 < last:
            m = (first+last)/2
            if A[m] < A[m-1]:
                last = m
            elif A[m] < A[m+1]:
                first = m
            else:
                last = m
        if A[first] < A[last]:
            return last
        return first

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())