#!/usr/bin/python
import sys

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        d = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            temp = {}
            for item in d:
                temp[item + nums[i]] = temp.get(item + nums[i], 0) + d.get(item, 0)
                temp[item - nums[i]] = temp.get(item - nums[i], 0) + d.get(item, 0)
            d = temp
        return d.get(S, 0)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())