#!/usr/bin/python
import sys

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        for n in nums:
            result += [i+[n] for i in result if i+[n] not in result]
        return result


def main():
    aa = Solution()
    print aa.subsetsWithDup()
    return 0

if __name__ == "__main__":
    sys.exit(main())
