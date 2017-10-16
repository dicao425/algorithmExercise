#!/usr/bin/python
import sys

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        l = 0
        r = 0
        min_length = float('INF')
        v = 0
        while r < len(nums):
            v += nums[r]
            r += 1
            while v >= s:
                min_length = min(min_length, r-l)
                v -= nums[l]
                l += 1
        if min_length == float('INF'):
            return 0
        return min_length

def main():
    aa = Solution()
    print aa.minSubArrayLen()
    return 0

if __name__ == "__main__":
    sys.exit(main())
