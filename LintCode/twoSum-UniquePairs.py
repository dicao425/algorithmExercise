#!/usr/bin/python
import sys


class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """

    def twoSum61(self, nums, target):
        # write your code here
        # Hashset
        result = set()
        h = set()
        c = 0
        for n in nums:
            if target - n in h:
                if (target - n, n) not in result and (n, target - n) not in result:
                    c += 1
                    result.add((n, target - n))
            h.add(n)
        return c

    def twoSum6(self, nums, target):
        # write your code here
        # two pointers
        nums.sort()
        i = 0
        j = len(nums) - 1
        result = 0
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                if (i == 0 or nums[i] != nums[i - 1]) and (j == len(nums) - 1 or nums[j] != nums[j + 1]):
                    result += 1
                i += 1
                j -= 1
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())