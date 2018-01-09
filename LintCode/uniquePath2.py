#!/usr/bin/python
import sys

class Solution:
    """
    @param: obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        y = len(obstacleGrid)
        x = len(obstacleGrid[0])
        matrix = [[0] * x for _ in range(y)]
        for i in range(x):
            if obstacleGrid[0][i] != 1:
                matrix[0][i] = 1
            else:
                break
        for j in range(y):
            if obstacleGrid[j][0] != 1:
                matrix[j][0] = 1
            else:
                break
        for j in range(1, y):
            for i in range(1, x):
                if obstacleGrid[j][i] == 1:
                    matrix[j][i] = 0
                else:
                    matrix[j][i] = matrix[j-1][i] + matrix[j][i-1]
        return matrix[-1][-1]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())