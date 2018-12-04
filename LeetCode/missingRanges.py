#!/usr/bin/python
import sys

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = [lower-1] + nums + [upper+1]
        result = []
        for i in range(len(nums)-1):
            left = nums[i]
            right = nums[i+1]
            if left != right - 1:
                if right - left == 2:
                    result.append(str(right - 1))
                elif right - left > 2:
                    result.append("{}->{}".format(left+1, right-1))
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())