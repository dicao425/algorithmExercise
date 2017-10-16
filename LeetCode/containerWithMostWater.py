#!/usr/bin/python
import sys

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        result = 0
        while l < r:
            result = max(result, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result

def main():
    aa = Solution()
    print aa.maxArea()
    return 0

if __name__ == "__main__":
    sys.exit(main())
