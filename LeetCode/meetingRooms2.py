#!/usr/bin/python
import sys

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        s_list = []
        e_list = []
        for i in intervals:
            s_list.append(i.start)
            e_list.append(i.end)
        s_list.sort()
        e_list.sort()
        ep = 0
        result = 0
        for i in range(len(intervals)):
            if s_list[i] < e_list[ep]:
                result += 1
            else:
                ep += 1
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())