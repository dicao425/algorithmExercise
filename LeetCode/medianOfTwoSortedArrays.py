#!/usr/bin/python
import sys


class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here
        l = len(A) + len(B)
        if l % 2 != 0:
            return self.findKth(A, B, l / 2 + 1)
        else:
            return (self.findKth(A, B, l / 2 + 1) + self.findKth(A, B, l / 2)) / 2.0

    def findKth(self, A, B, k):
        if not A:
            return B[k - 1]
        if not B:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        a = A[k / 2 - 1] if len(A) >= k / 2 else None
        b = B[k / 2 - 1] if len(B) >= k / 2 else None
        if b is None or (a is not None and a < b):
            return self.findKth(A[k / 2:], B, k - k / 2)
        return self.findKth(A, B[k / 2:], k - k / 2)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())