#!/usr/bin/python
import sys


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        length = len(costs)
        if length == 0:
            return 0
        pre = costs[0][:]
        curr = [0] * 3
        for i in range(length - 1):
            curr[0] = min(pre[1], pre[2]) + costs[i + 1][0]
            curr[1] = min(pre[0], pre[2]) + costs[i + 1][1]
            curr[2] = min(pre[0], pre[1]) + costs[i + 1][2]
            pre = curr[:]
        return min(pre)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())