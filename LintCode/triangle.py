#!/usr/bin/python
import sys

class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        result = triangle[-1][:]
        for r in range(len(triangle)-2, -1, -1):
            for i in range(len(triangle[r])):
                result[i] = min(result[i]+triangle[r][i], result[i+1]+triangle[r][i])
        return result[0]

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())