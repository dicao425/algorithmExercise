#!/usr/bin/python
import sys


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(T)
        for i, t in enumerate(T):
            if not stack:
                stack.append((t, i))
            else:
                while stack and t > stack[-1][0]:
                    result[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append((t, i))
        return result

def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())