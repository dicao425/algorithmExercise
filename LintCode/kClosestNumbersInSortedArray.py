#!/usr/bin/python
import sys

class Solution:
    """
    @param: A: an integer array
    @param: target: An integer
    @param: k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A:
            return -1
        first = 0
        last = len(A)-1
        while first + 1 < last:
            m = (first+last)/2
            if A[m] < target:
                first = m
            else:
                last = m
        if A[first] >= target:
            right = first
        elif A[last] >= target:
            right = last
        else:
            right = len(A)
        result = []
        left = right - 1
        for i in range(k):
            if left < 0:
                result.append(A[right])
                right += 1
            elif right == len(A):
                result.append(A[left])
                left -= 1
            else:
                if target - A[left] <= A[right] - target:
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())