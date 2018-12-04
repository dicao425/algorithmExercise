#!/usr/bin/python
import sys

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        stack = []
        i = 0
        while i < len(height):
            if not stack or height[stack[-1]] >= height[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                if not stack:
                    continue
                result += (min(height[stack[-1]], height[i]) - height[t]) * (i - stack[-1] - 1)
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())