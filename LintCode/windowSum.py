#!/usr/bin/python
import sys


class Solution:
    """
    @param: nums: a list of integers.
    @param: k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        if not nums:
            return []
        s = sum(nums[:k])
        result = [s]
        for i in range(len(nums) - k):
            j = i + k
            s = s - nums[i] + nums[j]
            result.append(s)
        return result


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())