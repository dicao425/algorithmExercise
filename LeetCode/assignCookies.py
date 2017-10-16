#!/usr/bin/python
import sys

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i]<=s[j]:
                i += 1
            j += 1
        return i

def main():
    aa = Solution()
    print aa.findContentChildren([1,2,3], [1,1])
    return 0

if __name__ == "__main__":
    sys.exit(main())
