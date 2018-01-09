#!/usr/bin/python
import sys


class Solution:
    """
    @param: nums: an integer array
    @param: target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        i = 0
        j = len(nums) - 1
        d = float('inf')
        while i < j:
            if nums[i] + nums[j] > target:
                d = min(d, nums[i] + nums[j] - target)
                j -= 1
            else:
                d = min(d, target - nums[i] - nums[j])
                i += 1
        return d


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())