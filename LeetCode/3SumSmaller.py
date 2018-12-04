#!/usr/bin/python
import sys


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    result += k - j
                    j += 1
                else:
                    k -= 1
        return result


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())