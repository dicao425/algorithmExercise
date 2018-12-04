#!/usr/bin/python
import sys

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = dict()
        for c in s:
            if c in d and d[c] == 1:
                d[c] = 0
            else:
                d[c] = 1
        return len([i for i in d.values() if i == 1]) <= 1

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())