#!/usr/bin/python
import sys

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target-n], i]
            else:
                d[n] = i
        return []

def main():
    aa = Solution()
    print aa.twoSum()
    return 0

if __name__ == "__main__":
    sys.exit(main())
