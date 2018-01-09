#!/usr/bin/python
import sys


class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        if n <= 2:
            return n
        dp = [1, 2]
        while n - 2:
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
            n -= 1
        return dp[1]

    def climbStairs1(self, n):
        # write your code here
        # rolling array
        f = [0, 1, 2]
        for i in range(3, n + 1):
            f[i % 3] = f[(i - 2) % 3] + f[(i - 1) % 3]
        return f[n % 3]


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())