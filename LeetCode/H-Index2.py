#!/usr/bin/python
import sys

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        l = 0
        r = length-1
        while l<=r:
            m = (l+r)/2
            if citations[m] >= length-m:
                r = m-1
            else:
                l = m+1
        return length-l

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())