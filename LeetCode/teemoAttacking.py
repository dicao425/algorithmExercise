#!/usr/bin/python
import sys

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        result = duration
        for i in range(1, len(timeSeries)):
            result += duration - max(0, timeSeries[i-1] + duration - timeSeries[i])
        return result

def main():
    aa = Solution()
    print aa.findPoisonedDuration()
    return 0

if __name__ == "__main__":
    sys.exit(main())
