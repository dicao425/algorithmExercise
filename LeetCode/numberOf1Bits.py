#!/usr/bin/python
import sys

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result += n%2
            n /= 2
        return result

def main():
    aa = Solution()
    print aa.hammingWeight(32)
    return 0

if __name__ == "__main__":
    sys.exit(main())
