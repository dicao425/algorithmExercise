#!/usr/bin/python
import sys


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers
    """

    def nextPermutation(self, nums):
        # write your code here
        if len(nums) <= 1:
            return nums
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums = self.reverse(i + 1, len(nums) - 1, nums)
                        break
                break
            else:
                if i == 0:
                    nums = self.reverse(0, len(nums) - 1, nums)
        return nums

    def reverse(self, s, e, nums):
        while s <= e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
        return nums

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())