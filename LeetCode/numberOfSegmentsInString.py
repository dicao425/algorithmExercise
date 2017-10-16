#!/usr/bin/python
import sys

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        return len(s.split())

def main():
    aa = Solution()
    print aa.countSegments()
    return 0

if __name__ == "__main__":
    sys.exit(main())
