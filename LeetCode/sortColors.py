#!/usr/bin/python
import sys

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        for n in xrange(len(nums)):
            v = nums[n]
            nums[n] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
        return
def main():
    aa = Solution()
    print aa.sortColors()
    return 0

if __name__ == "__main__":
    sys.exit(main())
