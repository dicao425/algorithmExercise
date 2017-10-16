#!/usr/bin/python
import sys

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n%2 == 0:
            n /= 2
        return n == 1

def main():
    aa = Solution()
    print aa.isPowerOfTwo()
    return 0

if __name__ == "__main__":
    sys.exit(main())
