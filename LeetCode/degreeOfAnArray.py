#!/usr/bin/python
import sys

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        m = 0
        for n in nums:
            d[n] = d.get(n, 0) + 1
            m = max(m, d[n])
        result = float('inf')
        reversed_nums = nums[::-1]
        can_nums = [k for k, v in d.items() if v == m]
        for n in can_nums:
            result = min(result, len(nums) - reversed_nums.index(n) - nums.index(n))
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())