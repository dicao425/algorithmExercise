#!/usr/bin/python
import sys

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        l = []
        for o in ops:
            if o == 'C':
                l.pop()
            elif o == 'D':
                l.append(l[-1]*2)
            elif o == '+':
                l.append(l[-1] + l[-2])
            else:
                l.append(int(o))
        return sum(l)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())