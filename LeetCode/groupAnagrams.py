#!/usr/bin/python
import sys

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in strs:
            k = ''.join(sorted(i))
            d[k] = d.get(k, []) + [i]
        return d.values()

def main():
    aa = Solution()
    print aa.groupAnagrams()
    return 0

if __name__ == "__main__":
    sys.exit(main())
