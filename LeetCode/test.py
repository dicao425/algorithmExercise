#!/usr/bin/python
import sys

class Solution(object):
    def __init__(self):
        self.data = [0] * 1000
        self.tot = 0
        self.sum = 0

    def insert(self, num):
        self.tot += 1
        self.data[num] += 1
        self.sum += num

    def getMean(self):
        if not self.tot:
            return 0
        return self.sum / float(self.tot)

    def getMedian(self):
        if not self.tot:
            return 0
        isEven = False
        mid = 0
        if self.tot % 2 == 0:
            isEven = True
            mid = self.tot / 2
        else:
            mid = self.tot / 2 + 1
            isEven = False
        v = 0
        for num, many in enumerate(self.data):
            v += many
            if v < mid:
                continue
            elif v > mid:
                return num
            else:
                if isEven:
                    idx = num+1
                    while self.data[idx] == 0:
                        idx += 1
                    return (num+idx) / 2.0
                else:
                    return num

def main():
    aa = Solution()
    import pdb
    pdb.set_trace()
    return 0

if __name__ == "__main__":
    sys.exit(main())