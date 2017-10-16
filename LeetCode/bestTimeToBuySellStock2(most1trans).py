#!/usr/bin/python
import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pro = 0
        minV = float('inf')
        for p in prices:
            minV = min(p, minV)
            pro = max(pro, p - minV)
        return pro

def main():
    aa = Solution()
    print aa.maxProfit([7,1,5,3,6,4])
    return 0

if __name__ == "__main__":
    sys.exit(main())
