#!/usr/bin/python
import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = -int(str(-x)[::-1]) if x < 0 else int(str(x)[::-1])
        if result > 2147483647 or result < -2147483648:
            return 0
        return result

def main():
    aa = Solution()
    print aa.reverse()
    return 0

if __name__ == "__main__":
    sys.exit(main())
