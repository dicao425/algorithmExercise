#!/usr/bin/python
import sys
class Solution:
    """
    @param: dividend: the dividend
    @param: divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        positive = (dividend < 0) is (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1
        if not positive:
            result = -result
        return min(max(-2147483648, result), 2147483647)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())