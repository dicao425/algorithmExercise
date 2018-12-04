#!/usr/bin/python
import sys


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[:k])
        result = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            result = max(result, s)
        return result * 1.0 / k


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())