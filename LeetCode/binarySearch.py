#!/usr/bin/python
import sys

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
