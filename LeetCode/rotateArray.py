#!/usr/bin/python
import sys

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(s, l, h):
            while l <= h:
                s[l], s[h] = s[h], s[l]
                l += 1
                h -= 1
            return
        n = len(nums)
        k = k % n
        reverse(nums, 0, n-k-1)
        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-1)
        return

def main():
    aa = Solution()
    print aa.rotate()
    return 0

if __name__ == "__main__":
    sys.exit(main())
