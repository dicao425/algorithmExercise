#!/usr/bin/python
import sys


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for i in (2, 3, 5):
            while num % i == 0:
                num /= i
        return num == 1



def main():
    aa = Solution()
    print aa.isUgly(6)
    return 0

if __name__ == "__main__":
    sys.exit(main())
