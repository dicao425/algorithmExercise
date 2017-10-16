#!/usr/bin/python
import sys


class Solution(object):
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for i in nums:
            x ^= i
        b = x & (-x)
        m = 0
        n = 0
        for i in nums:
            if i & b == 0:
                m ^= i
            else:
                n ^= i
        return [m, n]

    def singleNumber(self, nums):
        d = set()
        for i in nums:
            if i in d:
                d.remove(i)
            else:
                d.add(i)
        return list(d)


def main():
    aa = Solution()
    print aa.singleNumber()
    return 0

if __name__ == "__main__":
    sys.exit(main())
