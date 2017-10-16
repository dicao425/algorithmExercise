#!/usr/bin/python
import sys

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = sorted(nums)[len(nums)/2]
        return sum([abs(n-m) for n in nums])

def main():
    aa = Solution()
    print aa.minMoves2()
    return 0

if __name__ == "__main__":
    sys.exit(main())
