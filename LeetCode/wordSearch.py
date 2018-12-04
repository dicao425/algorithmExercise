#!/usr/bin/python
import sys


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if not word:
            return True
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1:
            return False
        if board[i][j] == word[0]:
            tmp = board[i][j]
            board[i][j] = '#'
            if self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) or self.dfs(board, i, j + 1,
                                                                                                      word[
                                                                                                      1:]) or self.dfs(
                    board, i, j - 1, word[1:]):
                return True
            board[i][j] = tmp
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