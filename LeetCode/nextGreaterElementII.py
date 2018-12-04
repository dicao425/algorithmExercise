#!/usr/bin/python
import sys

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums)
        stack = []
        for i in range(len(nums)) * 2:
            while stack and nums[i] > nums[stack[-1]]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())