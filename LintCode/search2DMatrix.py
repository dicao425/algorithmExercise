#!/usr/bin/python
import sys
class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        first = 0
        last = m*n - 1
        while first + 1 < last:
            mid = (first+last)/2
            x = mid % n
            y = mid / n
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                first = mid
            else:
                last = mid
        if matrix[first/n][first%n] == target:
            return True
        if matrix[last/n][last%n] == target:
            return True
        return False

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())