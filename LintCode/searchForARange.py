#!/usr/bin/python
import sys

class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
        first = 0
        last = len(A) - 1
        r1, r2 = -1, -1
        while first + 1 < last:
            m = (first+last)/2
            if A[m] < target:
                first = m
            else:
                last = m
        if A[first] == target:
            r1 = first
        elif A[last] == target:
            r1 = last
        else:
            return [r1, r2]
        first = 0
        last = len(A) - 1
        while first + 1 < last:
            m = (first+last)/2
            if A[m] > target:
                last = m
            else:
                first = m
        if A[last] == target:
            r2 = last
        elif A[first] == target:
            r2 = first
        else:
            return [-1, -1]
        return [r1, r2]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())