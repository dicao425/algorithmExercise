#!/usr/bin/python
import sys


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = len(B) / len(A)
        for i in range(3):
            if B in A * (times + i):
                return times + i
        return -1


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())