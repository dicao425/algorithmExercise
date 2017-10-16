#!/usr/bin/python
import sys

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        if len(nums) <= 2: return '/'.join(nums)
        return '{}/({})'.format(nums[0], '/'.join(nums[1:]))
'''
x1/x2/x3/x4/xn
x1/最小数
x1/x2 * 最大数
最大数 = x3*x4*x5...
'''
def main():
    aa = Solution()
    print aa.optimalDivision()
    return 0

if __name__ == "__main__":
    sys.exit(main())
