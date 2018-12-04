#!/usr/bin/python
import sys

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        return B in A+A

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())