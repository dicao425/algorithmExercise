#!/usr/bin/python
import sys

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        result = [[0] * (len(obstacleGrid[0])+1) for _ in range(len(obstacleGrid)+1)]
        result[1][1] = 1 - obstacleGrid[0][0]
        print result
        for i in range(1, len(result)):
            for j in range(1, len(result[0])):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    result[i][j] = 0
                else:
                    result[i][j] = result[i][j-1] + result[i-1][j]
        return result[-1][-1]


def main():
    aa = Solution()
    ll=[[0,0,0],[0,1,0],[0,0,0]]
    print aa.uniquePathsWithObstacles(ll)
    return 0

if __name__ == "__main__":
    sys.exit(main())
