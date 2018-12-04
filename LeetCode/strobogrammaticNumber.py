#!/usr/bin/python
import sys

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {'6': '9', '9': '6', '1': '1', '8': '8', '0': '0'}
        if set(num) - set(d.keys()):
            return False
        new = []
        for n in num:
            new.append(d[n])
        return num == ''.join(new[::-1])

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())