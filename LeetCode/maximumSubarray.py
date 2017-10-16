#!/usr/bin/python
import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curr = m = nums[0]
        for i in nums[1:]:
            curr = max(i, i + curr)
            m = max(m, curr)
        return m

def main():
    aa = Solution()
    print aa.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    return 0

if __name__ == "__main__":
    sys.exit(main())
