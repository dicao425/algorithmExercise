#!/usr/bin/python
import sys


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if set([a, b]) == set([2147483647, -2147483648]):
            return -1
        if a < 0 or b < 0:
            if a < 0:
                b, a = abs(a), b
            if b < 0:
                b = abs(b)
            return self.minus(a, b)
        elif a < 0 and b < 0:
            return self.allMinus(abs(a), abs(b))
        else:
            return self.add(a, b)

    def add(self, a, b):
        while b != 0:
            c = a & b
            a = a ^ b
            b = c << 1
        return a

    def minus(self, a, b):
        while b != 0:
            c = (~a) & b
            a = a ^ b
            b = c << 1
        return a

    def allMinus(self, a, b):
        return ~(self.add(a, b))


def main():
    aa = Solution()
    print aa.getSum(1, 2)
    return 0

if __name__ == "__main__":
    sys.exit(main())
