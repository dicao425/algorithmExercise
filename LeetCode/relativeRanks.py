#!/usr/bin/python
import sys

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        d = {}
        s = sorted(nums)[::-1]
        r = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(nums) + 1)]
        result = []
        for n in zip(s, r):
            d[n[0]] = n[1]
        for n in nums:
            result.append(d[n])
        return result

def main():
    aa = Solution()
    print aa.findRelativeRanks([5,4,3,2,1])
    return 0

if __name__ == "__main__":
    sys.exit(main())
