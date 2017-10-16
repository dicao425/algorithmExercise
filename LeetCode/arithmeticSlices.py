#!/usr/bin/python
import sys

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = [0, 0]
        i = 1
        for n in range(2, len(A)):
            if A[n] - A[n-1] == A[n-1] - A[n-2]:
                l.append(l[n-1]+i)
                i += 1
            else:
                l.append(l[n-1])
                i = 1
        return l[-1]

def main():
    aa = Solution()
    print aa.numberOfArithmeticSlices()
    return 0

if __name__ == "__main__":
    sys.exit(main())
