#!/usr/bin/python
import sys

class Solution:
    """
    @param: A: A an integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A:
            return 0
        p1 = None
        first = 0
        last = len(A)-1
        while first + 1 < last:
            m = (first+last)/2
            if A[m] < target:
                first = m
            else:
                last = m
        if A[first] == target:
            p1 = first
        elif A[last] == target:
            p1 = last
        else:
            return 0
        p2 = p1
        first = 0
        last = len(A) - 1
        while first + 1 < last:
            m = (first + last) / 2
            if A[m] > target:
                last = m
            else:
                first = m
        if A[last] == target:
            p2 = last
        elif A[first] == target:
            p2 = first
        return p2-p1+1

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())