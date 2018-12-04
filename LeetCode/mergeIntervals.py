#!/usr/bin/python
import sys

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        for i in sorted(intervals, key=lambda i: i.start):
            if result and i.start <= result[-1].end:
                result[-1].end = max(result[-1].end, i.end)
            else:
                result += i,    # result.append(i)
        return result


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution1(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        intervals.sort(key=lambda x: x.start)
        p1 = 0
        p2 = 1
        result = []
        while p2 < len(intervals):
            if intervals[p1].end >= intervals[p2].start:
                intervals[p1].end = max(intervals[p1].end, intervals[p2].end)
            else:
                result.append(intervals[p1])
                p1 = p2
            p2 += 1
        if p1 < len(intervals):
            result.append(intervals[p1])
        return result


def main():
    aa = Solution()
    print aa.merge()
    return 0

if __name__ == "__main__":
    sys.exit(main())
