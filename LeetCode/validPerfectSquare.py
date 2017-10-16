#!/usr/bin/python
import sys


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        t = num / 2
        while t * t > num:
            t = (t + num / t) / 2
        return t * t == num

        if num == 1:
            return True
        l = 1
        h = num / 2
        while l <= h:
            m = (l + h) / 2
            if m * m == num:
                return True
            if m * m < num:
                l = m + 1
                continue
            if m * m > num:
                h = m - 1
                continue
        return False


def main():
    aa = Solution()
    print aa.isPerfectSquare()
    return 0

if __name__ == "__main__":
    sys.exit(main())
