#!/usr/bin/python
import sys

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n:
            result = chr(ord('A') + (n-1)%26) + result
            n = (n-1) / 26
        return result


def main():
    aa = Solution()
    print aa.convertToTitle()
    return 0

if __name__ == "__main__":
    sys.exit(main())
