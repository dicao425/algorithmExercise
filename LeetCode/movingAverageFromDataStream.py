#!/usr/bin/python
import sys


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.q = []
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q) < self.size:
            self.q.append(val)
            self.sum += val
            return self.sum * 1.0 / len(self.q)
        else:
            self.sum -= self.q[0]
            self.sum += val
            self.q.pop(0)
            self.q.append(val)
            return self.sum * 1.0 / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

def main():
    aa = MovingAverage()
    return 0

if __name__ == "__main__":
    sys.exit(main())