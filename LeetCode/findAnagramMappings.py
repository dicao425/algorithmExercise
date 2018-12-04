#!/usr/bin/python
import sys

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = dict()
        for i, n in enumerate(B):
            d[n] = i
        result = [0] * len(A)
        for i, n in enumerate(A):
            if n in d:
                result[i] = d[n]
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())