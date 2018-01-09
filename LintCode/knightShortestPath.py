#!/usr/bin/python
import sys

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param: grid: a chessboard included 0 (false) and 1 (true)
    @param: source: a point
    @param: destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        dx = (1, 1, -1, -1, 2, 2, -2, -2)
        dy = (2, -2, 2, -2, 1, -1, 1, -1)
        q = [(source, 0)]
        while q:
            node, step = q.pop(0)
            if node.x == destination.x and node.y == destination.y:
                return step
            for i in range(8):
                nx = node.x+dx[i]
                ny = node.y+dy[i]
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny]:
                    continue
                grid[nx][ny] = 1
                q.append((Point(nx, ny), step+1))
        return -1

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())