#!/usr/bin/python
import sys

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.search(candidates, 0 ,target)

    def search(self, candidates, start, target):
        if target == 0:
            return [[]]
        result = []
        for i in xrange(start, len(candidates)):
            if i != start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            for r in self.search(candidates, i+1, target-candidates[i]):
                result.append([candidates[i]]+r)
        return result

def main():
    aa = Solution()
    print aa.combinationSum2()
    return 0

if __name__ == "__main__":
    sys.exit(main())
