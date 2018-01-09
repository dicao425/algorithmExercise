#!/usr/bin/python
import sys

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        self.result = []
        self.dfs(s, 0, [])
        return self.result

    def dfs(self, s, sidx, can):
        if len(s) == sidx:
            self.result.append(can[:])
            return
        for i in range(sidx, len(s)):
            new_s = s[sidx: i + 1]
            if not self.isPal(new_s):
                continue
            can.append(new_s)
            self.dfs(s, i + 1, can)
            can.pop()

    def isPal(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())