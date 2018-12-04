#!/usr/bin/python
import sys

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = min2 = float('inf')
        max1 = max2 = max3 = -float('inf')
        for n in nums:
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
            if n > max3:
                max1 = max2
                max2 = max3
                max3 = n
            elif n > max2:
                max1 = max2
                max2 = n
            elif n > max1:
                max1 = n
        return max(min1*min2*max3, max1*max2*max3)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())