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
