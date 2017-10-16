#!/usr/bin/python
import sys

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int('{0:032b}'.format(n)[::-1], 2)

def main():
    aa = Solution()
    print aa.reverseBits()
    return 0

if __name__ == "__main__":
    sys.exit(main())
