#!/usr/bin/python
import sys

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums)*len(nums)

def main():
    aa = Solution()
    print aa.minMoves([1,2,3])
    return 0

if __name__ == "__main__":
    sys.exit(main())
