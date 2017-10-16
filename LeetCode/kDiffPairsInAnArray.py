#!/usr/bin/python
import sys

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        d = set()
        result = set()
        for n in nums:
            if d:
                if n+k in d:
                    result.add((n, n+k))
                if n-k in d:
                    result.add((n-k, n))
            d.add(n)
        return len(result)

def main():
    aa = Solution()
    print aa.findPairs([6,3,5,7,2,3,3,8,2,4], 2)
    return 0

if __name__ == "__main__":
    sys.exit(main())
