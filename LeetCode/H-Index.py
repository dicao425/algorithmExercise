#!/usr/bin/python
import sys


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        length = len(citations)
        for i in range(length):
            if citations[i] >= length - i:
                return length - i
        return 0



def main():
    aa = Solution()
    print aa.hIndex()
    return 0

if __name__ == "__main__":
    sys.exit(main())
