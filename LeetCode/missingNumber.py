#!/usr/bin/python
import sys

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        result = 0
        for n in nums:
            result ^= n
            result ^= k
            k += 1
        result ^= k
        return result

def main():
    aa = Solution()
    print aa.missingNumber()
    return 0

if __name__ == "__main__":
    sys.exit(main())
