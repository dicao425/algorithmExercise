#!/usr/bin/python
import sys


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m + 1]:
                l += 2
            else:
                r = m
        return nums[l]


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())