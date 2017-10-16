#!/usr/bin/python
import sys

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hs = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n not in hs:
                hs.add(n)
            else:
                return False
        return True

def main():
    aa = Solution()
    print aa.isHappy(19)
    return 0

if __name__ == "__main__":
    sys.exit(main())
