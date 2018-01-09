#!/usr/bin/python
import sys

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        last = len(nums)-1
        while first+1 < last:
            m = (first+last)/2
            if nums[m] < nums[m-1]:
                last = m
            elif nums[m] < nums[m+1]:
                first = m
            else:
                last = m
        if nums[first] < nums[last]:
            return last
        return first

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())