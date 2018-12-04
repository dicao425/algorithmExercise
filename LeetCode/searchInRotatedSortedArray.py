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
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            m = (l + r) / 2
            if nums[m] > nums[-1]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m
            else:
                if nums[m] < target <= nums[r]:
                    l = m
                else:
                    r = m
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1

class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        first = 0
        last = len(nums) - 1
        while first + 1 < last:
            m = (first + last) / 2
            if nums[first] < nums[m]:
                if nums[first] <= target and nums[m] > target:
                    last = m
                else:
                    first = m
            else:
                if nums[last] >= target and nums[m] < target:
                    first = m
                else:
                    last = m
        if nums[first] == target:
            return first
        if nums[last] == target:
            return last
        return -1

def main():
    aa = Solution()
    print aa.search()
    return 0

if __name__ == "__main__":
    sys.exit(main())
