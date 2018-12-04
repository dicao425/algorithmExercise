#!/usr/bin/python
import sys

import itertools


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for ns in set(itertools.permutations(nums)):
            for ops in itertools.product((add, sub, mul, div), repeat=3):
                # (Z op (Y op (W op X)))
                result = ops[0](ns[0], ns[1])
                result = ops[1](ns[2], result)
                result = ops[2](ns[3], result)
                if 23.99 < result < 24.01:
                    return True

                # ((W op X) op (Y op Z))
                result1 = ops[0](ns[0], ns[1])
                result2 = ops[1](ns[2], ns[3])
                result = ops[2](result1, result2)
                if 23.99 < result < 24.01:
                    return True

        return False


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return 0
    return a / float(b)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())