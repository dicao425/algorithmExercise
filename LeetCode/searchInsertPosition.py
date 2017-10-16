#!/usr/bin/python
import sys

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        while l <= h:
            m = (h+l)/2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                h = m-1
        return l

def main():
    aa = Solution()
    print aa.searchInsert()
    return 0

if __name__ == "__main__":
    sys.exit(main())
