#!/usr/bin/python
import sys


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.preProcess = [0] + [sum(nums[:i + 1]) for i in range(len(nums))]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.preProcess[j + 1] - self.preProcess[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

def main():
    aa = NumArray()
    print aa.sumRange()
    return 0

if __name__ == "__main__":
    sys.exit(main())
