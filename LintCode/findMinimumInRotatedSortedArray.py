#!/usr/bin/python
import sys


class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1
        first = 0
        last = len(nums) - 1
        target = nums[-1]
        while first + 1 < last:
            m = (first + last) / 2
            if nums[m] <= target:
                last = m
            else:
                first = m
        return min(nums[first], nums[last])


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())