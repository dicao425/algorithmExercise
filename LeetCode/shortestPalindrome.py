#!/usr/bin/python
import sys

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        new = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(new[i:]):
                return new[:i]+s
def main():
    aa = Solution()
    print aa.shortestPalindrome()
    return 0

if __name__ == "__main__":
    sys.exit(main())
