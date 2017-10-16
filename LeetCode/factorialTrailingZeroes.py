#!/usr/bin/python
import sys

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #return 0 if n == 0 else n/5 + self.trailingZeroes(n/5)
        result = 0
        while n:
            n /= 5
            result += n
        return result

def main():
    aa = Solution()
    print aa.trailingZeroes()
    return 0

if __name__ == "__main__":
    sys.exit(main())
