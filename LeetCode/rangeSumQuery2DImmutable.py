#!/usr/bin/python
import sys


class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.c = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    self.c[i][j] = matrix[i][j]
                elif j == 0:
                    self.c[i][j] = matrix[i][j] + self.c[i - 1][j]
                elif i == 0:
                    self.c[i][j] = matrix[i][j] + self.c[i][j - 1]
                else:
                    self.c[i][j] = self.c[i - 1][j] + self.c[i][j - 1] + matrix[i][j] - self.c[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = self.c[row2][col2]
        if row1 > 0 and col1 > 0:
            result += self.c[row1 - 1][col1 - 1]
        if row1 > 0:
            result -= self.c[row1 - 1][col2]
        if col1 > 0:
            result -= self.c[row2][col1 - 1]
        return result


def main():
    aa = NumMatrix()
    print aa.sumRegion()
    return 0

if __name__ == "__main__":
    sys.exit(main())
