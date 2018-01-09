#!/usr/bin/python
import sys

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        j = -1
        for r in matrix:
            while j + len(r) and r[j] > target:
                j -= 1
            if r[j] == target:
                return True
        return False

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())