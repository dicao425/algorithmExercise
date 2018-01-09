#!/usr/bin/python
import sys

class Solution:
    """
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        matrix = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[-1][-1]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())