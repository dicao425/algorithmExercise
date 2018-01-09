#!/usr/bin/python
import sys

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        if not nums:
            return -1
        first = 0
        last = len(nums) - 1
        while first + 1 < last:
            m = (first+last)/2
            if nums[m] >= target:
                last = m
            else:
                first = m
        if nums[first] == target:
            return first
        if nums[last] == target:
            return last
        return -1

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())