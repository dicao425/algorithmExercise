#!/usr/bin/python
import sys
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        index = 0
        while reader.get(index) < target:
            index = index * 2 + 1
        first = 0
        last = index
        while first + 1 < last:
            m = (first+last)/2
            if reader.get(m) < target:
                first = m
            elif reader.get(m) > target:
                last = m
            else:
                last = m
        if reader.get(first) == target:
            return first
        if reader.get(last) == target:
            return last
        return -1

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())