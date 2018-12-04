#!/usr/bin/python
import sys

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        curr = int(time[:2]) * 60 + int(time[3:])
        numbers = {x for x in time if x != ":"}
        while True:
            curr = (curr + 1) % (24 * 60)
            next_hour = curr / 60
            next_min = curr % 60
            next_time_numbers = set("{:02d}".format(next_hour) + "{:02d}".format(next_min))
            if not next_time_numbers - numbers:
                return "{:02d}:{:02d}".format(next_hour, next_min)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())