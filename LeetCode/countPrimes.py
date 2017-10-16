#!/usr/bin/python
import sys

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in xrange(2, n):
            if res[i]:
                for j in xrange(2, (n-1)//i+1):
                    res[i*j] = False
        return sum(res)

def main():
    aa = Solution()
    print aa.countPrimes()
    return 0

if __name__ == "__main__":
    sys.exit(main())
