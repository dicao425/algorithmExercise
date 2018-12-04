#!/usr/bin/python
import sys

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B) or not A or not B or set(A) != set(B):
            return False
        pos = []
        for i in range(len(A)):
            if A[i] != B[i]:
                pos.append(i)
        if not pos and len(A) > len(set(A)):
            return True
        if len(pos) != 2:
            return False
        return (A[pos[0]], A[pos[1]]) == (B[pos[1]], B[pos[0]])

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())