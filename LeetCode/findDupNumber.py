#!/usr/bin/python
import sys


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# nums[0] ALWAYS the entrance, because no number 0 in it.
def main():
    aa = Solution()
    print aa.findDuplicate()
    return 0

if __name__ == "__main__":
    sys.exit(main())
