#!/usr/bin/python
import sys

class Solution(object):
    def wordSearch(self, board, word):
        self.board = board
        for j in range(len(board)):
            for i in range(len(board[0])):
                if self.dfs(i, j, word):
                    return True
        return False

    def dfs(self, i, j, word):
        if not word:
            return True
        if i<0 or j<0 or i>=len(self.board[0]) or j>=len(self.board):
            return False
        if self.board[j][i] == word[0]:
            tmp_ch, self.board[j][i] = self.board[j][i], '#'
            if self.dfs(i+1, j, word[1:]) or self.dfs(i, j+1, word[1:])\
                    or self.dfs(i-1, j, word[1:]) or self.dfs(i, j-1, word[1:]):
                return True
            self.board[j][i] = tmp_ch
        return False


def main():
    mm = [
        ['A', 'B', 'C', 'D'],
        ['B', 'B', 'R', 'A'],
        ['A', 'C', 'C', 'D'],
        ['A', 'B', 'S', 'D']
    ]
    word = 'BRA'
    aa = Solution()
    print aa.wordSearch(mm, word)
    return 0

if __name__ == "__main__":
    sys.exit(main())