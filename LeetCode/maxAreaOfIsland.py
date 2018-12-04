#!/usr/bin/python
import sys


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    result = max(result, area)
        return result

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.dfs(grid, i + 1, j) + self.dfs(grid, i, j + 1) + self.dfs(grid, i - 1, j) + self.dfs(grid,
                                                                                                                 i,
                                                                                                                 j - 1)
        return 0

class Solution1(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        area = [self.dfs(grid, i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        return max(area) if area else 0

    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.dfs(grid, i + 1, j) + self.dfs(grid, i - 1, j) + self.dfs(grid, i, j + 1) + self.dfs(grid, i, j - 1)
        return 0


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())