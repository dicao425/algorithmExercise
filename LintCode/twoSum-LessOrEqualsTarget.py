#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: an array of integer
    @param: target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        nums.sort()
        i = 0
        j = len(nums) - 1
        result = 0
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                result += j - i
                i += 1
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())