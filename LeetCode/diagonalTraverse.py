#!/usr/bin/python
import sys

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        entries = [(i+j, (j, i)[(i^j)&1], val)
               for i, row in enumerate(matrix)
               for j, val in enumerate(row)]
        return [e[2] for e in sorted(entries)]

def main():
    aa = Solution()
    print aa.findDiagonalOrder()
    return 0

if __name__ == "__main__":
    sys.exit(main())
