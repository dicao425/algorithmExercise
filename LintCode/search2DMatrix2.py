#!/usr/bin/python
import sys

class Solution:
    """
    @param: matrix: A list of lists of integers
    @param: target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        y = 0
        x = len(matrix[0])-1
        count = 0
        while x >= 0 and y < len(matrix):
            if matrix[y][x] == target:
                count += 1
                y += 1
                x -= 1
            elif matrix[y][x] < target:
                y += 1
            else:
                x -= 1
        return count

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())