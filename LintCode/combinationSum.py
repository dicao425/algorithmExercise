#!/usr/bin/python
import sys

class Solution:
    """
    @param: candidates: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
            return []
        self.result = []
        self.t = target
        candidates = sorted(list(set(candidates)))
        self.dfs(candidates, 0, [])
        return self.result

    def dfs(self, candidates, sidx, l):
        if sum(l) == self.t:
            self.result.append(l[:])
            return
        for i in range(sidx, len(candidates)):
            if sum(l) < self.t:
                l.append(candidates[i])
                self.dfs(candidates, i, l)
                l.pop()

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())