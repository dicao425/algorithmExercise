#!/usr/bin/python
import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in range(1, amount+1):
            min_c = MAX
            for c in coins:
                min_c = min(min_c, dp[i-c] if i-c >= 0 else MAX)
            dp[i] = min_c + 1
        if dp[-1] == MAX:
            return -1
        else:
            return dp[-1]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())