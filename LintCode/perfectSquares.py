#!/usr/bin/python
import sys

class Solution:
    """
    @param: n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        dp = [float('inf')] * (n + 1)
        i = 0
        while i*i <= n:
            dp[i * i] = 1
            i += 1
        for i in range(n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[-1]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())