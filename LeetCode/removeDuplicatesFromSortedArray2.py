#!/usr/bin/python
import sys


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i


def main():
    aa = Solution()
    print aa.removeDuplicates([1,1,1,2,2,3])
    return 0

if __name__ == "__main__":
    sys.exit(main())
