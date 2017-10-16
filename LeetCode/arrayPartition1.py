#!/usr/bin/python
import sys

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

def main():
    aa = Solution()
    print aa.arrayPairSum()
    return 0

if __name__ == "__main__":
    sys.exit(main())
