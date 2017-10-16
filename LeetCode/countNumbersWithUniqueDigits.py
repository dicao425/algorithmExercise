#!/usr/bin/python
import sys


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = 1
        p = 1
        for i in range(n if n <= 10 else 10):
            p *= choices[i]
            result += p
        return result

def main():
    aa = Solution()
    print aa.countNumbersWithUniqueDigits()
    return 0

if __name__ == "__main__":
    sys.exit(main())
