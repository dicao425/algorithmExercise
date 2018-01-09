#!/usr/bin/python
import sys

class Solution:
    """
    @param: A: an integer array sorted in ascending order
    @param: target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        if not A:
            return -1
        first = 0
        last = len(A)-1
        while first+1 < last:
            m = (first + last)/2
            if A[m] == target:
                return m
            elif A[m] < target:
                first = m
            else:
                last = m
        if target-A[first] > A[last]-target:
            return last
        return first

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())