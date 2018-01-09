#!/usr/bin/python
import sys

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
import numpy as np


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)
        result = 0
        for i in range(l):
            d = {'i': 1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y:
                    same += 1
                    continue
                if tx == points[i].x:
                    slope = 'i'
                else:
                    # slope = ((points[i].y-ty) * 1.0) / (points[i].x-tx)
                    slope = ((points[i].y - ty) * np.longdouble(1)) / (points[i].x - tx)
                if slope not in d:
                    d[slope] = 1
                d[slope] += 1
            result = max(result, max(d.values()) + same)
        return result


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())