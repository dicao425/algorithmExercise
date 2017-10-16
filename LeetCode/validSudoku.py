#!/usr/bin/python
import sys

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        result = []
        for i, c in enumerate(board):
            for j, n in enumerate(c):
                if n != '.':
                    result += [(n, i), (j, n), (i/3, j/3, n)]
        return len(result) == len(set(result))

def main():
    bb = [".87654321","2........","4........","...3.....","9........","6........","7........","8........","5........"]
    aa = Solution()
    print aa.isValidSudoku(bb)
    return 0

if __name__ == "__main__":
    sys.exit(main())