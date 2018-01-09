#!/usr/bin/python
import sys

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        first = 0
        last = len(nums)-1
        target = nums[-1]
        while first + 1 < last:
            m = (first+last)/2
            if nums[m] <= target:
                last = m
            else:
                first = m
        return min(nums[first], nums[last])

class Solution1(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        while l < h:
            m = l+(h-l)/2
            if nums[m] < nums[h]:
                h = m
            else:
                l = m+1
        return nums[l]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())