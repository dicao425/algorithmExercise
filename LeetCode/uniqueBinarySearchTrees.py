#!/usr/bin/python
import sys

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = 0
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

def main():
    aa = Solution()
    print aa.numTrees()
    return 0

if __name__ == "__main__":
    sys.exit(main())
