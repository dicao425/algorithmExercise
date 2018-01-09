#!/usr/bin/python
import sys

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        s = set(nums)
        for n in nums:
            if n-1 not in s:
                y = n + 1
                while y in s:
                    y += 1
                result = max(result, y-n)
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())