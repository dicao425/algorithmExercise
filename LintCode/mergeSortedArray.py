#!/usr/bin/python
import sys


class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        # From back to front
        i = m - 1
        j = n - 1
        idx = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] < B[j]:
                A[idx] = B[j]
                j -= 1
            else:
                A[idx] = A[i]
                i -= 1
            idx -= 1
        while j >= 0:
            A[j] = B[j]
            j -= 1


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())