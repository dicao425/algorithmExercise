#!/usr/bin/python
import sys


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in xrange(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(result):
                result = tmp
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(result):
                result = tmp
        return result

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]

def main():
    aa = Solution()
    print aa.longestPalindrome()
    return 0

if __name__ == "__main__":
    sys.exit(main())
