#!/usr/bin/python
import sys

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        for n in nums:
            result += [i+[n] for i in result]
        return result


def main():
    aa = Solution()
    print aa.subsets()
    return 0

if __name__ == "__main__":
    sys.exit(main())
