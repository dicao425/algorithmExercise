#!/usr/bin/python
import sys

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            v = abs(nums[i]) - 1
            if nums[v] > 0:
                nums[v] = - nums[v]
        result = []
        for i, n in enumerate(nums):
            if n > 0:
                result.append(i+1)
        return result

def main():
    aa = Solution()
    print aa.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    return 0

if __name__ == "__main__":
    sys.exit(main())
