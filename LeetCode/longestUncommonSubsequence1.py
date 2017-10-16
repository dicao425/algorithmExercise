#!/usr/bin/python
import sys

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))

def main():
    aa = Solution()
    print aa.findLUSlength()
    return 0

if __name__ == "__main__":
    sys.exit(main())
