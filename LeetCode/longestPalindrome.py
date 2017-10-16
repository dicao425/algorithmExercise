#!/usr/bin/python
import sys


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        result = 0
        single = False
        for l in s:
            d[l] = d.get(l, 0) + 1
        for v in d.values():
            if v % 2 == 0:
                result += v
            else:
                single = True
                if v != 1:
                    result += v - 1
        return result + (1 if single else 0)



def main():
    aa = Solution()
    print aa.longestPalindrome()
    return 0

if __name__ == "__main__":
    sys.exit(main())
