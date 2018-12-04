#!/usr/bin/python
import sys


class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        result = []
        pre = S[0]
        c = 0
        start = 0
        for i, s in enumerate(S):
            if pre is not None and s != pre:
                if c >= 3:
                    result.append([start, i - 1])
                start = i
                c = 1
                pre = s
            else:
                c += 1
        if c >= 3:
            result.append([start, i])
        return result


def main():
    aa = Solution()
    return 0

if __name__ == "__main__":
    sys.exit(main())