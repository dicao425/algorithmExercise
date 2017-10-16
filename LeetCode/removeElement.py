#!/usr/bin/python
import sys


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        b = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[b] = nums[i]
                b += 1
        return b


def main():
    aa = Solution()
    print aa.removeElement()
    return 0

if __name__ == "__main__":
    sys.exit(main())
