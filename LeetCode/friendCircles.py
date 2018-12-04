#!/usr/bin/python
import sys


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.visited = set()
        result = 0
        for n in range(len(M)):
            if n not in self.visited:
                self.dfs(M, n)
                result += 1
        return result

    def dfs(self, M, node):
        for idx, v in enumerate(M[node]):
            if v and idx not in self.visited:
                self.visited.add(idx)
                self.dfs(M, idx)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())