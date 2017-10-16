#!/usr/bin/python
import sys

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies)/2, len(set(candies)))

def main():
    aa = Solution()
    print aa.distributeCandies()
    return 0

if __name__ == "__main__":
    sys.exit(main())
