#!/usr/bin/python
import sys

class RecentCounter(object):

    def __init__(self):
        self.q = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.q and self.q[0] + 3000 < t:
            self.q.pop(0)
        self.q.append(t)
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

def main():
    aa = RecentCounter()
    return 0

if __name__ == "__main__":
    sys.exit(main())