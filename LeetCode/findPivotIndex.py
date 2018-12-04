#!/usr/bin/python
import sys

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        leftsum = 0
        for i, n in enumerate(nums):
            if leftsum == (s - leftsum - n):
                return i
            leftsum += n
        return -1

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())