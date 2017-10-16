#!/usr/bin/python
import sys


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        d = {}
        for i, l in enumerate(s):
            if l in d:
                d[l].append(i)
            else:
                d[l] = [i]
        for l in s:
            if len(d[l]) == 1:
                return d[l][0]
        return -1


def main():
    aa = Solution()
    print aa.firstUniqChar()
    return 0

if __name__ == "__main__":
    sys.exit(main())
