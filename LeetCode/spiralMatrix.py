#!/usr/bin/python
import sys


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.result = []
        self.helper(matrix)
        return self.result

    def helper(self, m):
        if m:
            self.result += m.pop(0)
            self.helper(self.rotate(m))

    def rotate(self, m):
        return zip(*m)[::-1]

def main():
    aa = Solution()
    print aa.spiralOrder([[1,2,3], [4,5,6], [7,8,9]])
    return 0

if __name__ == "__main__":
    sys.exit(main())
