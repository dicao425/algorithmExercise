#!/usr/bin/python
import sys


class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication1(self, nums):
        # write your code here
        # O(n)  O(n)
        h = set()
        c = 0
        for n in nums:
            if n not in h:
                h.add(n)
                nums[c] = n
                c += 1
        return c

    def deduplication(self, nums):
        # write your code here
        # O(nlogn) O(1)
        if not nums:
            return 0
        nums.sort()
        c = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[c] = nums[i]
                c += 1
        return c

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())