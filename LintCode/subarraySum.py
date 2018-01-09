#!/usr/bin/python
import sys


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        h = {0: -1}
        s = 0
        for i, n in enumerate(nums):
            s += n
            if s in h:
                return [h[s] + 1, i]
            h[s] = i
        return []

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())