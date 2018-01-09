#!/usr/bin/python
import sys

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h = 0
        v = 0
        for m in moves:
            if m == 'U':
                v += 1
            elif m == 'D':
                v -= 1
            elif m == 'L':
                h -= 1
            else:
                h += 1
        if v == 0 and h == 0:
            return True
        return False


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())