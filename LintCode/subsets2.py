#!/usr/bin/python
import sys

class Solution:
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        result = [[]]
        nums.sort()
        for i in nums:
            result += [n + [i] for n in result if n + [i] not in result]
        return result

def main():
    aa = Solution()
    print aa.subsetsWithDup([1, 2, 2])
    return 0

if __name__ == "__main__":
    sys.exit(main())