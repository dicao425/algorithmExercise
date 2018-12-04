#!/usr/bin/python
import sys
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        one = 1
        two = 2
        result = 0
        for i in range(3, n+1):
            result = one + two
            one = two
            two = result
        return result

def main():
    aa = Solution()
    print aa.climbStairs(4)
    return 0

if __name__ == "__main__":
    sys.exit(main())
