#!/usr/bin/python
import sys

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        x, y = zip(*ops)
        return min(x)*min(y)

def main():
    aa = Solution()
    print aa.maxCount()
    return 0

if __name__ == "__main__":
    sys.exit(main())
