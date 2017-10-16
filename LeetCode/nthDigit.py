#!/usr/bin/python
import sys

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, size, step = 1, 1, 9
        while n > size * step:
            n -= size * step
            size += 1
            step *= 10
            start *= 10
        return int(str(start + (n - 1) // size)[(n - 1) % size])

def main():
    aa = Solution()
    print aa.findNthDigit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
