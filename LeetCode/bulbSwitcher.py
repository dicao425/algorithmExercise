#!/usr/bin/python
import sys

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        k = 1
        while k**2 <= n:
            c += 1
            k += 1
        return c

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())