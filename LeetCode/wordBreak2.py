#!/usr/bin/python
import sys


class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        # write your code here
        self.s = s
        self.d = wordDict
        self.h = {}
        if not s or not self.dp():
            return []
        self.result = []
        self.dfs(0, [])
        return self.result

    def dfs(self, start, l):
        if start == len(self.s):
            self.result.append(' '.join(l))
            return
        # for i in range(start + 1, len(self.s) + 1):
        #     if self.s[start: i] in self.d:
        #         l.append(self.s[start: i])
        #         self.dfs(i, l)
        #         l.pop()
        if start in self.h:
            for i in self.h[start]:
                l.append(self.s[start: i])
                self.dfs(i, l)
                l.pop()

    def dp(self):
        l = [False] * (len(self.s) + 1)
        l[0] = True
        for i in range(1, len(self.s) + 1):
            for j in range(i):
                if l[j] and self.s[j: i] in self.d:
                    l[i] = True
                    self.h[j] = self.h.get(j, []) + [i]
        return l[-1]

def main():
    aa = Solution()
    print aa.wordBreak('lintcode', {'de', 'ding', 'co', 'code', 'lint'})
    return 0

if __name__ == "__main__":
    sys.exit(main())