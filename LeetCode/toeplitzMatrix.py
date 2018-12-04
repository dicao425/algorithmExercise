#!/usr/bin/python
import sys

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for l in range(m-1):
            if matrix[l][:n-1] != matrix[l+1][1:]:
                return False
        return True

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())