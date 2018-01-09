#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        result = nums[0]
        for n in nums:
            result = min(result, n)
        return result
# Special [1,1,1,1,1,1,0,1,1,1,1,1]
# Can not use BS to solve the special case, worse case O(n)
# best to solve in loop

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())