#!/usr/bin/python
import sys
import random

class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        n = 0
        result = -1
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                r = random.randint(0, n)
                n += 1
                if r == 0:
                    result = i
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

def main():
    aa = Solution()
    print aa.pick()
    return 0

if __name__ == "__main__":
    sys.exit(main())
