#!/usr/bin/python
import sys


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = nums[0]
        f = nums[n - 1]
        li = -2
        fi = -1
        for i in range(len(nums)):
            l = max(nums[i], l)
            f = min(nums[n - i - 1], f)
            if l > nums[i]:
                li = i
            if f < nums[n - i - 1]:
                fi = n - i - 1
        return li - fi + 1


def main():
    aa = Solution()
    print aa.findUnsortedSubarray()
    return 0

if __name__ == "__main__":
    sys.exit(main())
