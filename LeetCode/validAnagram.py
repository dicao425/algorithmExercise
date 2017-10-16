#!/usr/bin/python
import sys

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        for a in s:
            d1[a] = d1.get(a, 0) + 1
        for b in t:
            d2[b] = d2.get(b, 0) + 1
        return d1 == d2

def main():
    aa = Solution()
    print aa.isAnagram()
    return 0

if __name__ == "__main__":
    sys.exit(main())
