#!/usr/bin/python
import sys

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Node(object):
    def __init__(self, point, dis):
        self.point = point
        self.dis = dis

    def __cmp__(self, other):
        if self.dis != other.dis:
            return other.dis - self.dis
        if self.point.x != other.point.x:
            return other.point.x - self.point.x
        return other.point.y - self.point.y


class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        # write your code here
        import heapq
        heap = []
        for p in points:
            dist = self.get_distance(p, origin)
            heapq.heappush(heap, Node(p, dist))
            if len(heap) > k:
                heapq.heappop(heap)
        ret = []
        while heap:
            ret.append(heapq.heappop(heap).point)
        ret.reverse()
        return ret

    def get_distance(self, p1, p2):
        return (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())