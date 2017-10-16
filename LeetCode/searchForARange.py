#!/usr/bin/python
import sys

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def ss(n):
            l = 0
            r = len(nums)
            while l<r:
                m = (l+r)/2
                if nums[m] >= n:
                    r = m
                else:
                    l = m + 1
            return l
        low = ss(target)
        high = ss(target+1)
        if target in nums[low: low+1]:
            return [low, high-1]
        else:
            return [-1, -1]

def main():
    aa = Solution()
    print aa.searchRange()
    return 0

if __name__ == "__main__":
    sys.exit(main())
