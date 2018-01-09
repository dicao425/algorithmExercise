#!/usr/bin/python
import sys

"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
bad version.
"""


class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        # write your code here
        first = 1
        last = n
        while first + 1 < last:
            m = (first + last) / 2
            if SVNRepo.isBadVersion(m):
                last = m
            else:
                first = m
        if SVNRepo.isBadVersion(first):
            return first
        return last


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())