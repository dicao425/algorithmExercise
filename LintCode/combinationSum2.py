#!/usr/bin/python
import sys

class Solution:
    """
    @param: num: Given the candidate numbers
    @param: target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        # write your code here
        if not num:
            return []
        num.sort()
        self.t = target
        self.result = []
        self.dfs(num, 0, [])
        return self.result

    def dfs(self, num, sidx, l):
        if sum(l) == self.t and l not in self.result:
            self.result.append(l[:])
            return
        for i in range(sidx, len(num)):
            if sum(l) < self.t:
                l.append(num[i])
                self.dfs(num, i + 1, l)
                l.pop()

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())