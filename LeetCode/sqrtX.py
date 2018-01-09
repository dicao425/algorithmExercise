#!/usr/bin/python
import sys

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r

    def sqrt(self, x):
        # write your code here
        first = 1
        last = x
        while first + 1 < last:
            m = (first+last)/2
            if m * m == x:
                return m
            elif m * m < x:
                first = m
            else:
                last = m
        if first * first <= x:
            return first
        return last

def main():
    aa = Solution()
    print aa.mySqrt()
    return 0

if __name__ == "__main__":
    sys.exit(main())
