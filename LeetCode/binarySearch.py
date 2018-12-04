#!/usr/bin/python
import sys

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            m = (l+r) / 2
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m
            else:
                r = m
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1

class Search(object):
    def bs(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r+l)/2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return

class SearchMissing(object):
    def bs(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r+l)/2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return l

def main():
    aa = Search()
    print aa.bs([1,2,3,4,5,6], 4)
    bb = SearchMissing()
    print aa.bs([1, 2, 3, 5, 6], 4)
    return 0

if __name__ == "__main__":
    sys.exit(main())
