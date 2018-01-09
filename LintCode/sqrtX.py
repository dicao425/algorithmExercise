#!/usr/bin/python
import sys

class Solution:
    """
    @param: x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        first = 1
        last = x
        while first + 1 < last:
            m = (first+last)/2
            if m * m == x:
                return m
            elif m * m < x:
                first = m
            else:
                last = m
        if first * first <= x:
            return first
        return last

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())