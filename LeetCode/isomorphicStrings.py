#!/usr/bin/python
import sys

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def map(ss):
            d = {}
            for i, v in enumerate(ss):
                if v in d:
                    d[v].append(i)
                else:
                    d[v] = [i]
            return sorted(d.values())
        return map(s) == map(t)

def main():
    aa = Solution()
    print aa.isIsomorphic()
    return 0

if __name__ == "__main__":
    sys.exit(main())
