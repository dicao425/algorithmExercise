#!/usr/bin/python
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                p += prices[i+1]-prices[i]
        return p

def main():
    aa = Solution()
    print aa.maxProfit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
