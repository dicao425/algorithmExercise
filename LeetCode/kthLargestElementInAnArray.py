#!/usr/bin/python
import sys
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[k-1]


class SolutionQS(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        l = start
        r = end
        pivot = nums[(l + r) / 2]
        while l <= r:
            while l <= r and nums[l] > pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1
            if l <= r:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r -= 1
        if start + k - 1 <= r:
            return self.quickSelect(nums, start, r, k)
        if start + k - 1 >= l:
            return self.quickSelect(nums, l, end, k - (l - start))
        return nums[r + 1]
def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())