#!/usr/bin/python
import sys

'''
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f0 = 0
        f1 = 0
        for i in nums:
            f0, f1 = f1, max(f0+i, f1)
        return f1

def main():
    aa = Solution()
    print aa.rob([])
    return 0

if __name__ == "__main__":
    sys.exit(main())
