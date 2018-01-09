#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        first = 0
        last = len(nums)-1
        while first+1 < last:
            m = (first+last)/2
            if nums[m] == target:
                first = m
            elif nums[m] > target:
                last = m
            else:
                first = m
        if nums[last] == target:
            return last
        if nums[first] == target:
            return first
        return -1

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())