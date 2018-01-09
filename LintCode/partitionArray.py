#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        l = 0
        r = len(nums) - 1
        while l <= r:
            while l <= r and nums[l] < k:
                l += 1
            while l <= r and nums[r] >= k:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return l

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())