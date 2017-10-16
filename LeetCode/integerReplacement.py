#!/usr/bin/python
import sys
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2:
            return 1+min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        else:
            return 1+self.integerReplacement(n//2)
def main():
    aa = Solution()
    print aa.integerReplacement(123)
    return 0

if __name__ == "__main__":
    sys.exit(main())