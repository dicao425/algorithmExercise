#!/usr/bin/python
import sys


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        for n in nums:
            if n == target:
                return True
        return False

# Worse case is O(n) dup there so just use simple loop
def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())