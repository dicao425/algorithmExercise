#!/usr/bin/python
import sys


class Solution:
    """
    @param: x: a double
    @return: the square root of x
    """

    def sqrt(self, x):
        # write your code here
        first = 0.0
        last = x if x > 1.0 else 1.0
        while last - first > 1e-10:
            m = (first + last) / 2
            if m * m <= x:
                first = m
            else:
                last = m
        return first


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())