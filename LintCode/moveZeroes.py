#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: an integer array
    @return:
    """
    def moveZeroes(self, nums):
        # write your code here
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())