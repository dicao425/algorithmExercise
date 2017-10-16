#!/usr/bin/python
import sys

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'i':
                    board[i][j] = '0'
        return board

    def dfs(self, b, i, j):
        if i <0 or j < 0 or i >= len(b) or j >= len(b[0]):
            return False
        if b[i][j] == '0' and b[i][j] != 'i':
            b[i][j] = 'X'
            if not self.dfs(b, i+1, j) or not self.dfs(b, i-1, j) or not self.dfs(b, i, j+1) or not self.dfs(b, i, j-1):
                b[i][j] = 'i'
        return True

class Solution1(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        q = []
        for i in range(len(board)):
            self.bfs(board, i, 0, q)
            self.bfs(board, i, len(board[0])-1, q)
        for j in range(1, len(board[0])-1):
            self.bfs(board, 0, j, q)
            self.bfs(board, len(board)-1, j, q)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'i':
                    board[i][j] = 'O'
        return board

    def bfs(self, board, i, j, q):
        if board[i][j] == 'O':
            self.helper(board, i, j, q)
        while q:
            i, j = q.pop(0)
            self.helper(board, i+1, j, q)
            self.helper(board, i, j+1, q)
            self.helper(board, i-1, j, q)
            self.helper(board, i, j-1, q)
        return

    def helper(self, board, i, j, q):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
            return
        board[i][j] = 'i'
        q.append((i, j))
        return


def main():
    mm = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    aa = Solution1()
    print aa.solve(mm)
    return 0

if __name__ == "__main__":
    sys.exit(main())