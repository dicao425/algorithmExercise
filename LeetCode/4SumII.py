#!/usr/bin/python
import sys

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        h = dict()
        result = 0
        for a in A:
            for b in B:
                h[a+b] = h.get(a+b, 0) + 1
        for c in C:
            for d in D:
                if -c-d in h:
                    result += h[-c-d]
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())