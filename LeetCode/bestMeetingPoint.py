#!/usr/bin/python
import sys


class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum_row = map(sum, grid)
        sum_col = map(sum, zip(*grid))

        def get_result(l):
            i = -1
            j = len(l)
            left = right = 0
            d = 0
            while i != j:
                if left < right:
                    d += left
                    i += 1
                    left += l[i]
                else:
                    d += right
                    j -= 1
                    right += l[j]
            return d

        return get_result(sum_row) + get_result(sum_col)


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())