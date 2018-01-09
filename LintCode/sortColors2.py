#!/usr/bin/python
import sys


class Solution:
    """
    @param: colors: A list of integer
    @param: k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        print "-------"
        print colors
        idx = [0] * k
        for i in range(len(colors)):
            v = colors[i]
            colors[i] = k
            for n in range(k, 2, -1):
                if v < n:
                    colors[idx[n - 2]] = n - 1
                    idx[n - 2] += 1
            if v == 1:
                colors[idx[0]] = 1
                idx[0] += 1

        print colors
        print idx

def main():
    aa = Solution()
    aa.sortColors2([2,1,1,2,2], 2)
    aa.sortColors2([3,1,2,2,4,3,5], 5)
    aa.sortColors2([3, 2, 2, 1, 4], 4)
    return 0

if __name__ == "__main__":
    sys.exit(main())