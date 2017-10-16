#!/usr/bin/python
import sys

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        while area%w != 0:
            w -= 1
        return [area/w, w]

def main():
    aa = Solution()
    print aa.constructRectangle(4)
    return 0

if __name__ == "__main__":
    sys.exit(main())
