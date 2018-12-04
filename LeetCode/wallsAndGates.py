#!/usr/bin/python
import sys

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        q = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j))
        while q:
            i, j = q.pop(0)
            for x, y in (i+1, j), (i, j+1), (i-1, j), (i, j-1):
                if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] == 2147483647:
                    rooms[x][y] = rooms[i][j] + 1
                    q.append((x, y))

class Solution1(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)

    def dfs(self, rooms, i, j, d):
        if i < 0 or j < 0 or i >= len(rooms) or j >= len(rooms[0]) or rooms[i][j] == -1:
            return
        if rooms[i][j] == 2147483647:
            rooms[i][j] = d
        else:
            if rooms[i][j] < d:
                return
            rooms[i][j] = d
        self.dfs(rooms, i + 1, j, d + 1)
        self.dfs(rooms, i, j + 1, d + 1)
        self.dfs(rooms, i - 1, j, d + 1)
        self.dfs(rooms, i, j - 1, d + 1)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())