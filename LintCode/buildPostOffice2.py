#!/usr/bin/python
import sys


class Solution:
    """
    @param: grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        m = len(grid)
        n = len(grid[0])
        s = [[[set(), 0] for _ in range(n)] for _ in range(m)]
        nodes = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    nodes.append((i, j))
        c = len(nodes)
        dx = (1, 0, -1, 0)
        dy = (0, 1, 0, -1)
        for node in nodes:
            ny, nx = node
            dn = [(ny, nx, 1)]
            while dn:
                ny1, nx1, d = dn.pop(0)
                for i in range(4):
                    new_y = ny1 + dy[i]
                    new_x = nx1 + dx[i]
                    if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                        continue
                    if grid[new_y][new_x] == 0:
                        if (ny, nx) not in s[new_y][new_x][0]:
                            s[new_y][new_x][0].add((ny, nx))
                            s[new_y][new_x][1] += d
                            dn.append((new_y, new_x, d+1))
        result = None, float('inf')
        for i in range(m):
            for j in range(n):
                if len(s[i][j][0]) == c and s[i][j][1] < result[1]:
                    result = (i, j), s[i][j][1]
        return result[1] if result[0] is not None else -1
# write your code here

def main():
    aa = Solution()
    grid = [[0, 1, 0, 0, 0], [1, 0, 0, 2, 1], [0, 1, 0, 0, 0]]
    print aa.shortestDistance(grid)
    return 0

if __name__ == "__main__":
    sys.exit(main())