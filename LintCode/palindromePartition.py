#!/usr/bin/python
import sys

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):
        # write your code here
        if not s:
            return []
        self.result = []
        self.dfs(s, 0, [])
        return self.result

    def dfs(self, s, sidx, combination):
        if sidx == len(s):
            self.result.append(combination[:])
            return
        for i in range(sidx, len(s)):
            new_s = s[sidx:i + 1]
            if not self.isPal(new_s):
                continue
            combination.append(new_s)
            self.dfs(s, i + 1, combination)
            combination.pop()

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