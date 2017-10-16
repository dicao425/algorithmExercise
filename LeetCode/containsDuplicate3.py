#!/usr/bin/python
import sys

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        idx = sorted(range(len(nums)), key=lambda x: nums[x])
        for i in range(len(nums)-1):
            j = i + 1
            while j < len(nums) and nums[idx[j]] - nums[idx[i]] <= t:
                if abs(idx[i] - idx[j]) <= k:
                    return True
                j += 1
        return False

def main():
    aa = Solution()
    print aa.containsNearbyAlmostDuplicate()
    return 0

if __name__ == "__main__":
    sys.exit(main())
