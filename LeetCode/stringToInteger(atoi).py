#!/usr/bin/python
import sys

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str or len(str) == 0:
            return 0
        str = str.strip().split(' ')[0]
        sign = -1 if str[0] == '-' else 1
        if str[0] in ('+', '-'):
            str = str[1:]
        result = 0
        start = ord('0')
        for c in str:
            if c == ' ':
                continue
            if not c.isdigit():
                break
            result = result * 10 + (ord(c) - start)
        result *= sign
        if result > 2147483647:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648
        return result

def main():
    aa = Solution()
    print aa.myAtoi()
    return 0

if __name__ == "__main__":
    sys.exit(main())
