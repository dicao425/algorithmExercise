#!/usr/bin/python
import sys

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        result = 0
        c = 0
        g = False
        for seat in seats:
            if seat == 0:
                if not g:
                    g = True
                    c = 1
                else:
                    c += 1
                result = max(result, c)
            else:
                g = False
                c = 0
        return max((result+1)/2, seats.index(1), seats[::-1].index(1))

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())