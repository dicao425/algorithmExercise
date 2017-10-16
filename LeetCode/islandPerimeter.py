#!/usr/bin/python
import sys


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result += self.dfs(grid, i + 1, j) + self.dfs(grid, i, j + 1) + self.dfs(grid, i - 1, j) + self.dfs(grid, i, j - 1)
        return result

    def dfs(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
            return 1
        return 0

def main():
    aa = Solution()
    print aa.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
    return 0

if __name__ == "__main__":
    sys.exit(main())
