#!/usr/bin/python
import sys

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        for i in range(n):
            if knows(x, i):
                x = i
        for i in range(x):
            if knows(x, i):
                return -1
        for i in range(n):
            if not knows(i, x):
                return -1
        return x


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())