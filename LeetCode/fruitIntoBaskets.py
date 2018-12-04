#!/usr/bin/python
import sys


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        result = 0
        i = 0
        d = dict()
        for idx, t in enumerate(tree):
            d[t] = d.get(t, 0) + 1
            while len(d) > 2:
                d[tree[i]] -= 1
                if d[tree[i]] == 0:
                    del d[tree[i]]
                i += 1
            result = max(result, idx - i + 1)
        return result
# 最长只含2数字子序列

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())