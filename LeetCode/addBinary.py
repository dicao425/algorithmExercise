#!/usr/bin/python
import sys

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

def main():
    aa = Solution()
    print aa.addBinary()
    return 0

if __name__ == "__main__":
    sys.exit(main())
