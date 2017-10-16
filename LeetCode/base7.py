#!/usr/bin/python
import sys


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        neg = "" if num > 0 else "-"
        num = abs(num) if num < 0 else num
        result = ""
        while num:
            result = str(num % 7) + result
            num = num // 7
        return neg + result


def main():
    aa = Solution()
    print aa.convertToBase7(100)
    return 0

if __name__ == "__main__":
    sys.exit(main())
