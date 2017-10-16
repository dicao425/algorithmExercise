#!/usr/bin/python
import sys

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        ll = zip(*strs)
        c = 0
        for i in ll:
            if len(set(i)) == 1:
                c += 1
            else:
                break
        return strs[0][:c]


def main():
    aa = Solution()
    print aa.longestCommonPrefix()
    return 0

if __name__ == "__main__":
    sys.exit(main())
