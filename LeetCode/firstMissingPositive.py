#!/usr/bin/python
import sys

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        n = set(nums)
        for i in range(1, max(nums)+2):
            if i not in n:
                return i


def main():
    aa = Solution()
    print aa.firstMissingPositive()
    return 0

if __name__ == "__main__":
    sys.exit(main())
