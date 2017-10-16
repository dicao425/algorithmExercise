#!/usr/bin/python
import sys


class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenh, lenn = len(haystack), len(needle)
        if lenn == 0:
            return 0
        next, p = [-1] * (lenn), -1
        for i in range(1, lenn):
            while p >= 0 and needle[i] != needle[p + 1]:
                p = next[p]
            if needle[i] == needle[p + 1]:
                p = p + 1
            next[i] = p
        p = -1
        for i in range(lenh):
            while p >= 0 and haystack[i] != needle[p + 1]:
                p = next[p]
            if haystack[i] == needle[p + 1]:
                p = p + 1
            if p + 1 == lenn:
                return i - p
        return -1


def main():
    aa = Solution()
    print aa.strStr()
    return 0

if __name__ == "__main__":
    sys.exit(main())
