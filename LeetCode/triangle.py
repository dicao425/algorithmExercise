#!/usr/bin/python
import sys

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        result = triangle[-1][:]
        for r in range(len(triangle)-2, -1, -1):
            for i in range(len(triangle[r])):
                result[i] = min(result[i]+triangle[r][i], result[i+1]+triangle[r][i])
        return result[0]

def main():
    aa = Solution()
    print aa.minimumTotal()
    return 0

if __name__ == "__main__":
    sys.exit(main())
