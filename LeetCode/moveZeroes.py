#!/usr/bin/python
import sys

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        po = 0
        for n in nums:
            if n != 0:
                nums[po] = n
                po += 1
        for i in range(po, len(nums)):
            nums[i] = 0
        return

def main():
    aa = Solution()
    print aa.moveZeroes([0, 1, 0, 3, 12])
    return 0

if __name__ == "__main__":
    sys.exit(main())
