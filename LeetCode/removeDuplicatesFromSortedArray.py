#!/usr/bin/python
import sys


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        p = 0
        for i in range(1, len(nums)):
            if nums[p] != nums[i]:
                p += 1
                nums[p] = nums[i]
        return p + 1

def main():
    aa = Solution()
    print aa.removeDuplicates()
    return 0

if __name__ == "__main__":
    sys.exit(main())
