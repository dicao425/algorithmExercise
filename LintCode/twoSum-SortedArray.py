#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: an array of Integer
    @param: target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i]+nums[j] > target:
                j -= 1
            elif nums[i]+nums[j] < target:
                i += 1
            else:
                return [i+1, j+1]
        return []

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())