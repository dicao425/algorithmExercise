#!/usr/bin/python
import sys


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for r in range(len(A)):
            A[r] = A[r][::-1]
            for i in range(len(A[r])):
                A[r][i] = 1 if A[r][i] == 0 else 0
        return A


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())