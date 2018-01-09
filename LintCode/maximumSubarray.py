#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
        curr = nums[0]
        result = nums[0]
        for n in nums[1:]:
            curr = max(n, curr+n)
            result = max(result, curr)
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())