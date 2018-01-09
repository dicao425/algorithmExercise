#!/usr/bin/python
import sys

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        first = 0
        last = len(nums) - 1
        r1, r2 = -1, -1
        while first + 1 < last:
            m = (first+last)/2
            if nums[m] < target:
                first = m
            else:
                last = m
        if nums[first] == target:
            r1 = first
        elif nums[last] == target:
            r1 = last
        else:
            return [r1, r2]
        first = 0
        last = len(nums) - 1
        while first + 1 < last:
            m = (first+last)/2
            if nums[m] > target:
                last = m
            else:
                first = m
        if nums[last] == target:
            r2 = last
        elif nums[first] == target:
            r2 = first
        else:
            return [-1, -1]
        return [r1, r2]

def main():
    aa = Solution()
    print aa.searchRange()
    return 0

if __name__ == "__main__":
    sys.exit(main())
