#!/usr/bin/python
import sys


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.c = candidates
        self.t = target
        for i in range(len(self.c)):
            self.dfs(i, [])
        return self.result

    def dfs(self, i, r):
        if sum(r) + self.c[i] == self.t:
            self.result.append(r + [self.c[i]])
            return
        elif sum(r) + self.c[i] > self.t:
            return
        else:
            for k in range(i, len(self.c)):
                self.dfs(k, r + [self.c[i]])
        return

def main():
    aa = Solution()
    print aa.combinationSum([2,3,7], 7)
    return 0

if __name__ == "__main__":
    sys.exit(main())
