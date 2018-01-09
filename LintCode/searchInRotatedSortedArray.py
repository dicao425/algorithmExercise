#!/usr/bin/python
import sys

class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        first = 0
        last = len(A) - 1
        while first + 1 < last:
            m = (first+last)/2
            if A[first] < A[m]:
                if A[first] <= target and A[m] > target:
                    last = m
                else:
                    first = m
            else:
                if A[last] >= target and A[m] < target:
                    first = m
                else:
                    last = m
        if A[first] == target:
            return first
        if A[last] == target:
            return last
        return -1

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())