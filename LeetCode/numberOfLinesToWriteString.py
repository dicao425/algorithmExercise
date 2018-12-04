#!/usr/bin/python
import sys


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        width = 0
        for c in S:
            w = widths[ord(c) - 97]
            width += w
            if width > 100:
                lines += 1
                width = w
        return lines, width


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())