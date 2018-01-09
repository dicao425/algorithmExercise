#!/usr/bin/python
import sys


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    result += 1
        return result

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i] = grid[i][:j] + ["x"] + grid[i][j + 1:]
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
        return


class Solution1(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not len(grid) or not len(grid[0]):
            return 0
        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    result += 1
        return result

    def bfs(self, grid, i, j):
        dx = (1, 0, -1, 0)
        dy = (0, 1, 0, -1)
        q = [(i, j)]
        while q:
            p = q.pop()
            for direction in range(4):
                np = (p[0] + dx[direction], p[1] + dy[direction])
                if np[0] < 0 or np[1] < 0 or np[0] >= len(grid) or np[1] >= len(grid[0]):
                    continue
                if grid[np[0]][np[1]] == '1':
                    grid[np[0]][np[1]] = '0'
                    q.append(np)

def main():
    aa = Solution()
    print aa.numIslands()
    return 0

if __name__ == "__main__":
    sys.exit(main())
