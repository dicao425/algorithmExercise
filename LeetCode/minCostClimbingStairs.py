#!/usr/bin/python
import sys

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 2:
            return min(cost)
        for i in range(2, len(cost)):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[-1], cost[-2])

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())