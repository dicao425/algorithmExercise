#!/usr/bin/python
import sys

class Solution(object):
    def canWinNim(self, n):
        """
            :type n: int
            :rtype: bool
            """
        return bool(n%4)
def main():
    aa = Solution()
    print aa.canWinNim(4)
    return 0

if __name__ == "__main__":
    sys.exit(main())
