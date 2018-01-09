#!/usr/bin/python
import sys

class Solution:
    """
    @param: grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((j, i))
        dx = (1, 0, -1, 0)
        dy = (0, -1, 0, 1)
        days = 0
        while q:
            days += 1
            nq = []
            for n in q:
                for di in range(4):
                    nx = n[0] + dx[di]
                    ny = n[1] + dy[di]
                    if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid) or grid[ny][nx] != 0:
                        continue
                    grid[ny][nx] = 1
                    nq.append((nx, ny))
            q = nq[:]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return -1
        return days-1

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())