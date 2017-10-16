#!/usr/bin/python
import sys

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        c = 0
        for i in s:
            if i == 'A':
                a += 1
                c = 0
            elif i == 'L':
                l += 1
                c += 1
                if c > 2:
                    return False
            else:
                c = 0
        if a <= 1:
            return True
        return False

def main():
    aa = Solution()
    print aa.checkRecord()
    return 0

if __name__ == "__main__":
    sys.exit(main())
