#!/usr/bin/python
import sys

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        result = []
        for i in range(len(nums)):
            result.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= p
            p *= nums[i]
        return result

class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        l2r = []
        for i in range(len(nums)):
            l2r.append(p)
            p *= nums[i]
        p = 1
        r2l = []
        for i in range(len(nums)-1, -1, -1):
            r2l.insert(0, p)
            p *= nums[i]
        result = []
        for i in range(len(nums)):
            result.append(l2r[i] * r2l[i])
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())