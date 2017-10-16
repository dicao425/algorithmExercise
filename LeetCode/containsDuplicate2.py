#!/usr/bin/python
import sys

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, n in enumerate(nums):
            if n in d and i - d[n] <= k:
                return True
            d[n] = i
        return False

def main():
    aa = Solution()
    print aa.containsNearbyDuplicate()
    return 0

if __name__ == "__main__":
    sys.exit(main())
