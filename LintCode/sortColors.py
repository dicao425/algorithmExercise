#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        i = 0
        j = 0
        for n in range(len(nums)):
            v = nums[n]
            nums[n] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())