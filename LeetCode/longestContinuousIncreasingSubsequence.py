#!/usr/bin/python
import sys

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        pre = nums[0]
        cnt = 1
        result = 1
        for i in range(1, len(nums)):
            if nums[i] <= pre:
                pre = nums[i]
                result = max(result, cnt)
                cnt = 1
            else:
                pre = nums[i]
                cnt += 1
        result = max(result, cnt)
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())