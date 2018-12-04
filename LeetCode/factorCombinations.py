#!/usr/bin/python
import sys

import math


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 2:
            return []
        self.result = []
        self.n = n
        self.dfs(2, n, [])
        return self.result

    def dfs(self, start, remain, l):
        if remain == 1:
            self.result.append(l[:])
            return
        for i in range(start, remain+1):
            if remain % i == 0:
                self.dfs(i, remain / i, l + [i])


    def getFactors1(self, n):
        todo, combis = [(n, 2, [])], []
        while todo:
            n, i, combi = todo.pop()
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n / i],
                    todo += (n / i, i, combi + [i]),
                i += 1
        return combis

def main():
    aa = Solution()
    print(aa.getFactors(32))
    print(aa.getFactors(23848713))
    return 0

if __name__ == "__main__":
    sys.exit(main())