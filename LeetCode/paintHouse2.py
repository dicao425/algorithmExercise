#!/usr/bin/python
import sys

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        num_colors = len(costs[0])
        curr = [0] * num_colors
        pre = costs[0][:]
        for i in range(len(costs)-1):
            for color in range(num_colors):
                curr[color] = min([pre[cc] for cc in [o for o in range(num_colors) if o != color]]) + costs[i+1][color]
            pre = curr[:]
        return min(pre)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())