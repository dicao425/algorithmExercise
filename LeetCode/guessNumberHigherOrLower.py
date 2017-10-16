#!/usr/bin/python
import sys


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    g = 6
    if num == g:
        return 0
    if num > g:
        return -1
    if num < g:
        return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l < h:
            m = (l + h) / 2
            if guess(m) == 1:
                l = m + 1
            else:
                h = m
        return l



def main():
    aa = Solution()
    print aa.guessNumber(10)
    return 0

if __name__ == "__main__":
    sys.exit(main())
