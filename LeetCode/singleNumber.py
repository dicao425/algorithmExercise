#!/usr/bin/python
import sys
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result ^= i
        return result
def main():
    aa = Solution()
    print aa.singleNumber([1,2,2,3,3,1,5])
    return 0

if __name__ == "__main__":
    sys.exit(main())
