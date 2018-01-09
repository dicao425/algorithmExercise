#!/usr/bin/python
import sys

class Solution:
    """
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        y = len(grid)
        x = len(grid[0])
        for i in range(1, x):
            grid[0][i] += grid[0][i-1]
        for j in range(1, y):
            grid[j][0] += grid[j-1][0]
        for j in range(1, y):
            for i in range(1, x):
                grid[j][i] += min(grid[j-1][i], grid[j][i-1])
        return grid[-1][-1]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())