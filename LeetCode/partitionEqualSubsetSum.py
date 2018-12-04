#!/usr/bin/python
import sys


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort(reverse=True)
        self.cache = dict()
        if sum(nums) % 2:
            return False
        return self.dfs(nums, 0, sum(nums) / 2)

    def dfs(self, nums, start, target):
        if (start, target) in self.cache:
            return self.cache[(start, target)]
        if target < 0:
            return False
        if target == 0:
            return True
        for i in range(start, len(nums)):
            if self.dfs(nums, i + 1, target - nums[i]):
                return True
        self.cache[(start, target)] = False
        return False


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())