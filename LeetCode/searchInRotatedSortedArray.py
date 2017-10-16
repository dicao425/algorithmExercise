#!/usr/bin/python
import sys

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        length = len(nums)
        if length == 1:
            return 0 if target in nums else -1
        p = length - 1
        for i in range(length-1):
            if nums[i] > nums[i+1]:
                p = i
                break
        m = 0
        r = p
        l = p + 1
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = length - 1
        else:
            return m
        m = (l+r)/2
        while l <= r:
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
            m = (r+l)/2
        return -1

def main():
    aa = Solution()
    print aa.search()
    return 0

if __name__ == "__main__":
    sys.exit(main())
