#!/usr/bin/python
import sys
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while n > 0:
            if n >= i:
                n -= i
                if n < i+1:
                    return i
                i += 1
            else:
                return i
        return 0

def main():
    aa = Solution()
    print aa.arrangeCoins()
    return 0

if __name__ == "__main__":
    sys.exit(main())
