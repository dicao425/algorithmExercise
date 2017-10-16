#!/usr/bin/python
import sys

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        x = len(board)
        y = len(board[0])
        if x == 0 or y == 0:
            return 0
        result = 0
        for i in range(x):
            for j in range(y):
                result += board[i][j] == 'X' and (i == 0 or board[i-1][j] != 'X') and (j == 0 or board[i][j-1] != 'X')
        return result

def main():
    aa = Solution()
    print aa.countBattleships()
    return 0

if __name__ == "__main__":
    sys.exit(main())
