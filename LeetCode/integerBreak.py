#!/usr/bin/python
import sys
class Solution(object):
    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n == 5:
            return 6
        if n == 6:
            return 9
        return 3 * self.integerBreak(n-3)

def main():
    aa = Solution()
    print aa.integerBreak(10)
    return 0

if __name__ == "__main__":
    sys.exit(main())
