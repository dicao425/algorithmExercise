#!/usr/bin/python
import sys


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1



def main():
    aa = Solution()
    print aa.isPowerOfFour()
    return 0

if __name__ == "__main__":
    sys.exit(main())
