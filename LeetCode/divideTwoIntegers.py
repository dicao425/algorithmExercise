#!/usr/bin/python
import sys


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2147483647
        neg = True if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else False
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        rest = 0
        count = 1
        d = divisor
        while dividend >= divisor:
            if dividend >= d:
                dividend -= d
                result += count
                d = d << 1
                count = count << 1
            else:
                d = d >> 1
                count = count >> 1
        if neg:
            result = - result
        return min(max(result, -2147483648), 2147483647)


def main():
    aa = Solution()
    print aa.divide(15, 3)
    return 0

if __name__ == "__main__":
    sys.exit(main())