#!/usr/bin/python
import sys


class Solution:
    """
    @param: n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            u = min(u2, u3, u5)
            if u == u2:
                i2 += 1
            if u == u3:
                i3 += 1
            if u == u5:
                i5 += 1
            ugly.append(u)
            n -= 1
        return ugly[-1]


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())