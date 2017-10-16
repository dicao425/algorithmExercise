#!/usr/bin/python
import sys

class Solution(object):
    def __init__(self):
        self.data = [0] * 1000
        self.sum = 0
        self.count = 0

    def insert(self, num):
        self.count += 1
        self.sum += num
        self.data[num] += 1

    def getMean(self):
        if not self.count:
            return 0
        return self.sum/float(self.count)

    def getMedian(self):
        if not self.count:
            return 0
        c = 0
        even = False
        if self.count % 2 == 0:
            mid = self.count / 2
            even = True
            # even
        else:
            mid = self.count / 2+1
            even = False
            # odd
        for idx, v in enumerate(self.data):
            c += v
            if c < mid:
                continue
            elif c > mid:
                return idx
            else:
                if even:
                    idx2 = idx+1
                    while self.data[idx2]==0:
                        idx2 += 1
                    return (idx+idx2)/2.0
                else:
                    return idx


def main():
    aa = Solution()
    import pdb
    pdb.set_trace()
    return 0

if __name__ == "__main__":
    sys.exit(main())