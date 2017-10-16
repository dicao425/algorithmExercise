#!/usr/bin/python
import sys

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n%3 == 0:
            n /= 3
        return n == 1

'''
Or simply hard code it since we know maxPowerOfThree = 1162261467:

public boolean isPowerOfThree(int n) {
    return n > 0 && (1162261467 % n == 0);
}
'''

def main():
    aa = Solution()
    print aa.isPowerOfThree()
    return 0

if __name__ == "__main__":
    sys.exit(main())
