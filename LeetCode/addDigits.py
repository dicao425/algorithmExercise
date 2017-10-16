#!/usr/bin/python
import sys

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return (num-1)%9+1

def main():
    aa = Solution()
    print aa.addDigits(38)
    return 0

if __name__ == "__main__":
    sys.exit(main())
