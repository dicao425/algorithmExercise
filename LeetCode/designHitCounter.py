#!/usr/bin/python
import sys


class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = 0
        self.q = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.q or self.q[-1][0] != timestamp:
            self.q.append([timestamp, 1])
        else:
            self.q[-1][1] += 1
        self.hits += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.q and self.q[0][0] <= timestamp - 300:
            self.hits -= self.q[0][1]
            self.q.pop(0)
        return self.hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())