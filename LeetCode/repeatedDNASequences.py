#!/usr/bin/python
import sys


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = set()
        hs = set()
        for i in range(len(s) - 9):
            subs = s[i:i + 10]
            if subs in hs:
                result.add(subs)
            else:
                hs.add(subs)
        return list(result)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())