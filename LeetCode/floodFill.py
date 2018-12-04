#!/usr/bin/python
import sys

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # BFS
        if image[sr][sc] == newColor:
            return image
        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)
        q = [(sr, sc)]
        o = image[sr][sc]
        while q:
            x, y = q.pop()
            image[x][y] = newColor
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= len(image) or ny >= len(image[0]):
                    continue
                if image[nx][ny] == o:
                    q.append((nx, ny))
        return image

    def floodFill1(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # Recursive DFS
        if image[sr][sc] == newColor:
            return image
        o = image[sr][sc]
        self.nc = newColor
        self.dfs(image, sr, sc, o)
        return image

    def dfs(self, image, i, j, o):
        if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
            return
        if image[i][j] == o:
            image[i][j] = self.nc
            self.dfs(image, i - 1, j, o)
            self.dfs(image, i, j - 1, o)
            self.dfs(image, i + 1, j, o)
            self.dfs(image, i, j + 1, o)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())