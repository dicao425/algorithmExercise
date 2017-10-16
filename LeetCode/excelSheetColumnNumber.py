#!/usr/bin/python
import sys


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s) - 1
        result = 0
        ordA = ord('A')
        for i in s:
            result += (ord(i) - ordA + 1) * 26 ** length
            length -= 1
        return result


def main():
    aa = Solution()
    print aa.titleToNumber()
    return 0

if __name__ == "__main__":
    sys.exit(main())
