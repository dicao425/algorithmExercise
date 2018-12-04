#!/usr/bin/python
import sys


class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row = [0] * n
        self.col = [0] * n
        self.n = n
        self.d1 = 0
        self.d2 = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        add_num = 1 if player == 1 else -1
        self.row[row] += add_num
        self.col[col] += add_num
        if row == col:
            self.d1 += add_num
        if row + col == self.n - 1:
            self.d2 += add_num
        if self.n in (abs(self.row[row]), abs(self.col[col]), abs(self.d1), abs(self.d2)):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())