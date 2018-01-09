#!/usr/bin/python
import sys

class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)
                    result += 1
        return result

    def bfs(self, grid, i, j):
        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)
        q = [(i, j)]
        while q:
            p = q.pop()
            for direction in range(4):
                np = (p[0] + dx[direction], p[1] + dy[direction])
                if np[0] < 0 or np[1] < 0 or np[0] >= len(grid) or np[1] >= len(grid[0]):
                    continue
                if grid[np[0]][np[1]] == 1:
                    grid[np[0]][np[1]] = 0
                    q.append(np)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())