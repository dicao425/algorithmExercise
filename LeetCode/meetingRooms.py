#!/usr/bin/python
import sys


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x.start)
        result = []
        for i in intervals:
            if result and result[-1].end > i.start:
                return False
            else:
                result.append(i)
        return True


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())