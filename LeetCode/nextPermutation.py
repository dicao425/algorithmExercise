#!/usr/bin/python
import sys
'''
From r to l, find 1st digit which violate the increase trend;
From r to l, find 1st digit which larger then the one from 1
Swap these two numbers
reverse all from the number 1 (not include this one, right after)
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def rev(start, end, l):
            while start <= end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1
            return l
        if not nums or len(nums) == 1:
            return
        length = len(nums)
        i = length - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i <= 0:
            nums = rev(0, length-1, nums)
            return
        j = length - 1
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[j], nums[i-1] = nums[i-1], nums[j]
        nums = rev(i, length-1, nums)
        return

def main():
    aa = Solution()
    print aa.nextPermutation()
    return 0

if __name__ == "__main__":
    sys.exit(main())
