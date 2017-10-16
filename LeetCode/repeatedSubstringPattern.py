#!/usr/bin/python
import sys


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s * 2)[1:-1]



def main():
    aa = Solution()
    print aa.repeatedSubstringPattern("abcabc")
    return 0

if __name__ == "__main__":
    sys.exit(main())
